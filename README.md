- [Grocery Delivery Software](#grocery-delivery-software)
  * [Usage](#usage)
  * [Screenshots](#screenshots)
  * [Requests](#requests)
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

1. Write Chrome extension so that users don't have to install Python locally and run the script from the command line.
2. Add easy to use email and SMS server so that users don't have to set up their own.
3. Add Amazon Fresh (maybe other delivery platforms?).
4. Maybe write Android and iOS apps?

## References

* [Pooja Ahuja's Whole Foods delivery slot script](https://github.com/pcomputo/Whole-Foods-Delivery-Slot)
* [Build a Bot to Get Notifications for Available Delivery Slots on Amazon Fresh](https://medium.com/better-programming/build-amazonfresh-delivery-slot-alerts-c9e12a429e23)
