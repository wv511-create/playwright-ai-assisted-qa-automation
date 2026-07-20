# Exploratory Testing Session Notes

**Application:** Namma-Yantra Share (Web Prototype)

**Session Duration:** 30 Minutes

## Scope

* Farmer Registration
* Machine Browsing
* Booking Flow
* My Bookings

## Registration

* Tested empty and invalid input fields.
* Application accepted invalid phone numbers and arbitrary text.
* No input validation was enforced.

## Machine Browsing

* Machine cards displayed correctly with images, names, pricing, and booking status.
* Machine category filters were non-functional.
* Search functionality did not filter machine results.

## Booking Flow

* Successfully created a booking.
* Cancel Booking button did not function.
* Invalid booking information was accepted.
* Rental duration increment/decrement controls were non-functional.

## My Bookings

* Booking appeared in the Pending section.
* Accepted and Declined tabs were not clickable.
* Refreshing the page redirected the user to the registration page.
* Previously created bookings were not retained after re-login.

## Summary

A total of 10 functional defects were identified during exploratory testing. Most issues were related to missing input validation, navigation, state persistence, and non-functional UI controls.

