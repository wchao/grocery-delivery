- [Grocery Delivery Software](#grocery-delivery-software)
  * [Usage](#usage)
    + [Installation](#installation)
    + [Configuration](#configuration)
  * [Screenshots](#screenshots)
  * [Requests](#requests)
  * [Issues](#issues)
  * [References](#references)

# Grocery delivery software

Like many people during COVID-19 who use grocery delivery services, I spend lots of time trying to reserve a delivery time slot on grocery delivery sites (FreshDirect, Amazon Fresh, Instacart). I wrote this software so I could get a time slot without sitting around refreshing the page for hours.

## Usage

Supports **MacOS, Linux, and Windows** (theoretically, though Windows is currently the only tested platform).

The script works on **Chrome**. Add Firefox if enough demand for it.

### Installation

1. Clone the project.
2. Install Python 3 if you don't already have it.
3. Install required Python modules using requirements.txt (```pip install -r requirements.txt```).
4. Create freshdirect_slot.ini configuration file using the template below in the Configuration section.
5. Run freshdirect_slot_chrome.py (```python freshdirect_slot_chrome.py```).

### Configuration

Create a freshdirect_slot.ini configuration file in the same directory that you put freshdirect_slot_chrome.py and adhering to the following template:

```
[freshdirect]
emit_debug_msg = True
user_data_dir = C:\Users\jsmith\AppData\Local\Google\Chrome\User Data
user_agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36
# after this number of refreshes, restart Chrome to deal with memory leaks and resource accumulation.
max_iterations_before_restart = 120
time_refresh_wait = 60
# after time slots are found, wait this amount of time to refresh the page to get all the time slots.
# sometimes the time slots are added over a few seconds, and the initial page load only catches a few.
# waiting a few seconds and then refreshing helps pick up all the available time slots.
time_found_refresh_wait = 30
smtp_server = mailserverhostname
smtp_username = mailserverusername
smtp_password = mailserverpassword
# email alerts come from this email. ensure that your mail server allows this, and that you have SPF and DKIM set up.
email_from = freshdirect_alert@mymailserver.com
# send email alerts to this email address. can be multiple emails separated by commas.
email_to = smith@yahoo.com
# where to dump HTML files. 
page_dump_dir = C:\Users\jsmith\Documents
```

Replace the values of user_data_dir, smtp_server, smtp_username, smtp_password, email_from, email_to, and page_dump_dir. For user_data_dir and page_dump_dir, the default Windows directory structure would be C:\\Users\\logon_name, so just replace jsmith with your logon name. The current version of the script requires that you have access to an email server (SMTP server) that authenticates with a username and password. Hopefully will add a feature to send mail without requiring the user to set up his own mail server soon.

## Screenshots

> __Screen 1__
![FreshDirect Chrome in action](https://github.com/wchao/grocery-delivery/blob/master/doc/img/freshdirect_slot_chrome_in_action.png)
> __Screen 2__
```
This is what an email alert looks like:

-----Original Message-----
From: abc@xyz.com
Sent: Thursday, April 16, 2020 12:42 PM
To: John Smith <smith@yahoo.com>
Subject: FreshDirect delivery time slot available

FreshDirect delivery time slots opened up at 2020-04-16 12:41:26:
Apr 19 6 am - 9 am
Apr 19 9 am - 12 pm
Apr 19 12 pm - 2 pm
Apr 19 2 pm - 5 pm
Apr 19 5 pm - 8 pm
Apr 19 8 pm - 10 pm
```

## Requests

1. Need better documentation for how to install and configure.
2. Write Chrome extension so that users don't have to install Python locally and run the script from the command line.
3. Add easy to use email and SMS server so that users don't have to set up their own. Maybe add Microsoft Outlook integration so that users can send email alerts to themselves using Outlook? Pretty easy to do on Windows with pywin32 and would eliminate need for separate mail server.
4. Add ability to check out and pay for order, in addition to current alerting capability. That way user doesn't have to wake up or do anything in response to an alert. The program will just place the order when a slot comes available. This would be useful when time slots open up in the middle of the night. I'm sure some people stay up late to get time slots.
5. Add Amazon Fresh (maybe also other delivery services like Peapod, Instacart, Shipt, Walmart, Postmates?).
6. Super order portal where user can specify what groceries they want, and the software places an order from the first available delivery service that has that basket of goods? This seems very ambitious and lots of things to figure out, but the benefit is that it is useful even after pandemic is over because there are out of stock items all the time at various grocers, and there will always be logistical issues with one delivery service being able to deliver sooner than another.
7. Perhaps add Firefox extension.
8. Maybe write Android and iOS apps?

## Issues

1. I am a FreshDirect Chef's Table customer, so I built the code in that environment. Does the reserve time slot page work if you are not Chef's Table? I don't know, but happy to work with someone who is not Chef's Table to troubleshoot and get it working in that environment.
2. If you get the error "PermissionError: [Errno 13] Permission denied: 'C:\\Users\\wchao\\.wdm\\drivers\\chromedriver\\81.0.4044.69\\win32\\chromedriver.exe'", then it probably means chromedriver.exe is still running and has a lock on the file that prevents it from being overwritten with the newest version. To fix this, start Task Manager and find the chromedriver process and right click and choose "End task". Then you should be able to run the freshdirect_slot_chrome.py program.

## References

* [Pooja Ahuja's Whole Foods delivery slot script](https://github.com/pcomputo/Whole-Foods-Delivery-Slot)
* [Build a Bot to Get Notifications for Available Delivery Slots on Amazon Fresh](https://medium.com/better-programming/build-amazonfresh-delivery-slot-alerts-c9e12a429e23)
* [Amazon Fresh Whole Foods delivery slot finder for Mac](https://github.com/ahertel/Amazon-Fresh-Whole-Foods-delivery-slot-finder)
