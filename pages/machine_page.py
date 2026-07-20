from playwright.sync_api import Page, expect


class MachinePage:

    def __init__(self, page: Page):
        self.page = page

    def verify_machine_page(self):
        expect(
            self.page.get_by_role(
                "textbox",
                name="Search machines..."
            )
        ).to_be_visible()

    def verify_categories(self):
        expect(self.page.get_by_text("All", exact=True)).to_be_visible()
        expect(self.page.get_by_text("Tractor", exact=True)).to_be_visible()
        expect(self.page.get_by_text("Harvester", exact=True)).to_be_visible()

    def book_first_machine(self):
        self.page.get_by_role("button", name="Book Now").first.click()