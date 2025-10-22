from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DemoQAAlerts(BasePage):
    alert_btn = (By.ID, "alertButton")  # Example

    def trigger_alert(self):
        self.click(self.alert_btn)
        self.handle_alert()
