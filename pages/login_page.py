from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("http://localhost:3000")

    def login_as_farmer(self, name, phone, village):
        self.page.get_by_role("textbox", name="Full Name").fill(name)
        self.page.get_by_role("textbox", name="Phone Number").fill(phone)
        self.page.get_by_role("textbox", name="Village").fill(village)
        self.page.get_by_text("Farmer").click()