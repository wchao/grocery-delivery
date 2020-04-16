import configparser
import os
import bs4
import re
import time
import smtplib
import email.message

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def detectTimeSlot(productUrl):
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument(f"--user-data-dir={conf['user_data_dir']}")
  chrome_options.add_argument(f"user-agent={conf['user_agent']}")
  chrome_options.add_argument("start-maximized")
  driver = None
  num_refreshes = 0
  found_open_slot = False
  found_during_previous_iteration = False
  div_list = []
  time_slot_list = []
  while not found_open_slot:
    if num_refreshes > int(conf['max_iterations_before_restart']):
      if conf.getboolean('emit_debug_msg'):
        print("Browser restarted at " + current_time())
      driver.close()
      driver = None
      num_refreshes = 0
    if not driver:
      driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
      driver.get(productUrl)
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, features='html.parser')
    # check if there are any time slots displayed on the page. Sometimes FreshDirect will display a schedule page with no
    # time slots, just empty except header and footer. In that case, we need to click on Sign out, then Sign in, and then load
    # the reservation page again. Or, it is possible FreshDirect is asking for us to log in for the first time.
    raw_div_list = soup.find_all('div', {'id': re.compile('ts_d\d+_ts\d+_time'), 'class': 'tsCont'})
    if not raw_div_list:
      # no time slot table displayed on page, so search for sign in button.
      if soup.find('input', {'id': 'signinbtn'}):
        # found sign in button, so it is initial log in.
        # click the sign in button (should already be populated by Chrome autofill/password manager.
        driver.find_element_by_id("signinbtn").click()
        if conf.getboolean('emit_debug_msg'):
          print("Signed in at " + current_time())
        # technically clicking the sign in button should bring us to the page we were originally requesting, but just safer to
        # explicitly load the page we want.
        driver.get(productUrl)
        num_refreshes += 1
      else:
        # soup.find returns None when element/tag is not found; that means we are already logged in.
        # avoid throwing an exception from driver.find_element_by_id by searching for the button before trying to click it.
        found_sign_in_button = False
        while not found_sign_in_button:
          # go to sign out page.
          driver.get('https://www.freshdirect.com/logout.jsp?logoutPage=site_access')
          # navigate to login page.
          driver.get('https://www.freshdirect.com/login/login.jsp')
          html = driver.page_source
          soup = bs4.BeautifulSoup(html, features='html.parser')
          if soup.find('input', {'id': 'signinbtn'}):
            found_sign_in_button = True
          else:
            if conf.getboolean('emit_debug_msg'):
              print("Time slot table not found. Tried to sign out and sign back in at " + current_time() + '. Sign in button not found. Trying again.')
        # click sign in button to log in.
        # Chrome autofill/password manager will fill in the email and password.
        driver.find_element_by_id("signinbtn").click()
        if conf.getboolean('emit_debug_msg'):
          print("Time slot table not found, so signed out and then signed back in at " + current_time())
        # navigate to reservation page.
        driver.get(productUrl)
        num_refreshes += 1
      # reset flag about found time slot during previous iteration.
      found_during_previous_iteration = False
      # loop around again to parse new page.
      continue
    # class is "fleft tsCont tsSoldoutC" when time slot is sold out, but only "fleft tsCont" or "fleft tsCont tsEcoFriendlyTimeC"
    # when not sold out. just because it is not sold out does not mean it is available. Some table cells are blank, so not
    # sold out, but not available either. class is "fleft tsCont tsReservationTimeE" when time slot is reserved under Chef's Table,
    # so that also will not match, which is how we want it since we don't want to issue an alert for a time slot we already have
    # reserved.
    raw_div_list = soup.find_all('div', {'id': re.compile('ts_d\d+_ts\d+_time'), 'class': lambda x: x and 'fleft' in x and 'tsCont' in x and 'tsSoldoutC' not in x and 'tsReservationTimeE' not in x})
    # certain <div> elements only have &nbsp; as content because they do not show a crossed-out time slot, so omit those.
    div_list.clear()
    for div in raw_div_list:
      # skip over div elements that only have &nbsp; ('\xa0') because they are not available time slots.
      if len(div.contents) == 1 and div.contents[0] == '\xa0':
        pass
      else:
        # potentially an available time slot, so add it.
        div_list.append(div)
    # check if div_list contains an available time slot.
    if div_list:
      if found_during_previous_iteration:
        found_open_slot = True
        for div in div_list:
          # id will be ts_dX_tsY_time, and we want X to find the <div> tag with id ts_dX_hC and the child div with class tsDayDateC,
          # which will contain the month and day.
          time_slot_day_index = div['id'][4:5]
          day_div = soup.find('div', {'id': 'ts_d' + time_slot_day_index + '_hC'})
          month_and_day = day_div.find('div', {'class': 'tsDayDateC'}).contents[0]
          time_slot_list.append(month_and_day + ' ' + div.contents[0])
      else:
        # found time slots initially, but wait for specified delay and then refresh and test if the time slots are still available.
        # this prevents phantom time slots that just appear for a few seconds, and also lets us capture all the time slots rather
        # than hastily alerting to just one or a few.
        found_during_previous_iteration = True
        if conf.getboolean('emit_debug_msg'):
          print('Found time slots initially at ' + current_time() + '. sleeping for a bit, then refreshing to see if time slots still there.')
        time.sleep(int(conf['time_found_refresh_wait']))
        driver.refresh()
        num_refreshes += 1
    else:
      # if no time slots, reset found flag, sleep, then refresh page.
      found_during_previous_iteration = False
      time.sleep(int(conf['time_refresh_wait']))
      driver.refresh()
      num_refreshes += 1
      if conf.getboolean('emit_debug_msg'):
        print('Refreshed at ' + current_time() + '. count = ' + str(num_refreshes))
  driver.close()
  driver.quit()
  if conf.getboolean('emit_debug_msg'):
    print('Found open time slots at ' + current_time() + ':')
    for time_slot in time_slot_list:
      print(time_slot)
  email_alert(time_slot_list)
  # save dump of page source to troubleshoot problems in this script.
  # to avoid UnicodeEncodeError, can use either open(filename, 'w', encoding='utf-8') or print(html.encode('utf-8'), file=f).
  f = open(conf['page_dump_dir'] + os.sep + time.strftime("%Y%m%d%H%M", time.localtime()) + ' freshdirect_dump.html', 'w', encoding='utf-8')
  print(html, file=f)
  f.close()

def current_time():
  return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def email_alert(time_slot_list):
  email_msg = email.message.EmailMessage()
  email_body = 'FreshDirect delivery time slots opened up at ' + current_time() + ':\n'
  for time_slot in time_slot_list:
    email_body += time_slot + '\n'
  email_msg.set_content(email_body)
  email_msg['Subject'] = 'FreshDirect delivery time slot available'
  email_msg['From'] = conf['email_from']
  email_msg['To'] = conf['email_to']
  smtp_conn = smtplib.SMTP(conf['smtp_server'])
  smtp_conn.starttls()
  smtp_conn.login(conf['smtp_username'], conf['smtp_password'])
  smtp_conn.send_message(email_msg)
  smtp_conn.quit()

top_config = configparser.ConfigParser()
top_config.read('freshdirect_slot.ini')
conf = top_config['freshdirect']
detectTimeSlot('https://www.freshdirect.com/your_account/reserve_timeslot.jsp')
