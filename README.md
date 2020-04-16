- [Grocery Delivery Software](#grocery-delivery-software)
  * [Usage](#usage)
  * [Screenshots](#screenshots)
  * [Requests](#requests)
  * [Issues](#issues)
  * [References](#references)

# Grocery delivery software

Like many people during COVID-19, I spend lots of time trying to reserve a delivery time slot on grocery delivery sites (FreshDirect, Amazon Fresh, Instacart). I wrote this software so I could get a time slot without sitting around refreshing the page for hours.

## Usage

Supports **MacOS, Linux, and Windows**.

The script works on **Chrome**.

1. Clone the project.
1. Run the requirements.txt (```$ pip install -r requirements.txt```).
2. Run freshdirect_slot_chrome.py (``` $ python freshdirect_slot_chrome.py```).

## Screenshots

> __Screen 1__
![FreshDirect Chrome in action](https://github.com/wchao/grocery-delivery/blob/master/doc/img/freshdirect_slot_chrome_in_action.png)
> __Screen 2__
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

## Requests

1. Need much better documentation for how to install and configure. In particular, add structure and format of freshdirect_slot.ini.
2. Write Chrome extension so that users don't have to install Python locally and run the script from the command line.
3. Add easy to use email and SMS server so that users don't have to set up their own. Maybe add Microsoft Outlook integration so that users can send email alerts to themselves using Outlook? Pretty easy to do on Windows with pywin32 and would eliminate need for separate mail server.
4. Add ability to check out and pay for order, in addition to current alerting capability. That way user doesn't have to wake up or do anything in response to an alert. The program will just place the order when a slot comes available.
5. Add Amazon Fresh (maybe other delivery platforms like Peapod, Instacart, Shipt, Walmart?).
6. Super order portal where user can specify what groceries they want, and the software places an order from the first available delivery service that has that basket of goods? This seems very ambitious and lots of things to figure out, but the benefit is that it is useful even after pandemic is over because there are out of stock items all the time at various grocers, and there will always be logistical issues with one delivery service being able to deliver sooner than another.
7. Maybe write Android and iOS apps?

## Issues

1. I am a FreshDirect Chef's Table customer, so I built the code in that environment. Does the reserve time slot page work if you are not Chef's Table? I don't know, but happy to work with someone who is not Chef's Table to troubleshoot and get it working in that environment.

## References

* [Pooja Ahuja's Whole Foods delivery slot script](https://github.com/pcomputo/Whole-Foods-Delivery-Slot)
* [Build a Bot to Get Notifications for Available Delivery Slots on Amazon Fresh](https://medium.com/better-programming/build-amazonfresh-delivery-slot-alerts-c9e12a429e23)
