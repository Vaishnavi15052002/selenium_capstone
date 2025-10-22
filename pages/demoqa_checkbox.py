from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DemoQACheckbox:
    def __init__(self, driver):
        self.driver = driver
        self.expand_all = (By.CSS_SELECTOR, "button[aria-label='Expand all']")
        self.checkbox_titles = (By.CLASS_NAME, "rct-title")

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

        # Hide ads to prevent click interception
        self.driver.execute_script("""
            let ads = document.querySelectorAll('iframe, [id^="google_ads"]');
            ads.forEach(ad => ad.style.display = 'none');
        """)
        time.sleep(2)

    def expand_all_checkboxes(self):
        """Expands all checkboxes on the page"""
        wait = WebDriverWait(self.driver, 10)
        expand_btn = wait.until(EC.element_to_be_clickable(self.expand_all))
        try:
            expand_btn.click()
        except Exception as e:
            print("⚠️ Click intercepted, using JavaScript click instead:", e)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", expand_btn)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", expand_btn)
        time.sleep(2)

    def select_checkbox(self, option_name):
        """Find and click the checkbox with matching label"""
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(self.checkbox_titles))

        for el in elements:
            if el.text.strip().lower() == option_name.lower():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
                try:
                    el.click()
                    print(f"✅ Selected checkbox: {option_name}")
                except Exception as e:
                    print("⚠️ Click failed, trying JS click:", e)
                    self.driver.execute_script("arguments[0].click();", el)
                break
        else:
            raise Exception(f"❌ Checkbox with name '{option_name}' not found!")
        time.sleep(2)
