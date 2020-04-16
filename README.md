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

## Requests

1. Need much better documentation for how to install and configure. In particular, add structure and format of freshdirect_slot.ini.
2. Write Chrome extension so that users don't have to install Python locally and run the script from the command line.
3. Add easy to use email and SMS server so that users don't have to set up their own.
4. Add ability to check out and pay for order, in addition to current alerting capability. That way user doesn't have to wake up or do anything in response to an alert. The program will just place the order when a slot comes available.
4. Add Amazon Fresh (maybe other delivery platforms like Peapod, Instacart, Shipt, Walmart?).
5. Maybe write Android and iOS apps?

## Issues

1. I am a FreshDirect Chef's Table customer, so I built the code in that environment. Does the reserve time slot page work if you are not Chef's Table? I don't know, but happy to work with someone who is not Chef's Table to troubleshoot and get it working in that environment.

## References

* [Pooja Ahuja's Whole Foods delivery slot script](https://github.com/pcomputo/Whole-Foods-Delivery-Slot)
* [Build a Bot to Get Notifications for Available Delivery Slots on Amazon Fresh](https://medium.com/better-programming/build-amazonfresh-delivery-slot-alerts-c9e12a429e23)
