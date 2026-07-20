from playwright.sync_api import Page, expect


class BookingPage:

    def __init__(self, page: Page):
        self.page = page

    def confirm_booking(self):
        expect(self.page.get_by_text("Confirm")).to_be_visible()
        self.page.get_by_role("button", name="Confirm").click()

    def verify_pending_booking(self):
        expect(
            self.page.get_by_text("Pending").first
        ).to_be_visible()

    def open_bookings(self):
        self.page.get_by_text("Bookings", exact=True).click()

    def verify_cancel_button(self):
        expect(
            self.page.get_by_role("button", name="Cancel").first
        ).to_be_visible()