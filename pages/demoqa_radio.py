from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class DemoQARadio(BasePage):
    yes_radio = (By.XPATH, "//label[text()='Yes']")
    impressive_radio = (By.XPATH, "//label[text()='Impressive']")
    no_radio = (By.XPATH, "//label[text()='No']")

    def open_url(self, url):
        """Open DemoQA Radio Button page and hide ads"""
        self.driver.get(url)
        self.driver.maximize_window()
        # Hide any Google ads or overlays
        self.driver.execute_script("""
            let ads = document.querySelectorAll('iframe, [id^="google_ads"]');
            ads.forEach(ad => ad.style.display = 'none');
        """)
        time.sleep(1)

    def select_radio(self, option):
        """Select a radio option by name (yes, impressive, or no)"""
        option = option.lower()

        # Map option name to locator
        radio_map = {
            "yes": self.yes_radio,
            "impressive": self.impressive_radio,
            "no": self.no_radio
        }

        if option not in radio_map:
            raise ValueError(f"Invalid option: {option}")

        locator = radio_map[option]
        element = self.wait.until(lambda d: d.find_element(*locator))

        # Check if it's disabled
        if "disabled" in element.get_attribute("class").lower():
            print(f"⚠️ '{option.upper()}' radio button is disabled, skipping click.")
            return

        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            print(f"✅ Clicked '{option.upper()}' radio button successfully.")
        except Exception as e:
            print(f"⚠️ Normal click failed for '{option}', using JS click instead: {e}")
            self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
