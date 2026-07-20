from pages.login_page import LoginPage
from pages.machine_page import MachinePage
from pages.booking_page import BookingPage


def test_booking_machine(page):

    login = LoginPage(page)
    machine = MachinePage(page)
    booking = BookingPage(page)

    login.open()
    login.login_as_farmer(
        "Ani",
        "9876543210",
        "Bangalore"
    )

    machine.book_first_machine()

    booking.confirm_booking()
    booking.verify_pending_booking()