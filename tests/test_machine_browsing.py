from pages.login_page import LoginPage
from pages.machine_page import MachinePage


def test_machine_browsing(page):

    login = LoginPage(page)
    machine = MachinePage(page)

    login.open()
    login.login_as_farmer(
        "Ani",
        "9876543210",
        "Bangalore"
    )

    machine.verify_machine_page()
    machine.verify_categories ()
