from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DemoQADropdown(BasePage):
    dropdown = (By.ID, "oldSelectMenu")  # Example

    def select_option(self, option_text):
        select = Select(self.driver.find_element(*self.dropdown))
        select.select_by_visible_text(option_text)
