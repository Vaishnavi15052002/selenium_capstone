from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DemoQAMultipleWindows:
    def __init__(self, driver):
        self.driver = driver
        self.new_tab_btn = (By.ID, "tabButton")

    def open_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(f"⚠️ Primary site failed ({e}), using fallback URL...")
            self.driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open")
        self.driver.maximize_window()

    def click_new_tab(self):
        """Handles both demoqa & w3schools"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.new_tab_btn)
            ).click()
        except Exception:
            # Fallback: handle w3schools "Try it" button
            self.driver.switch_to.frame("iframeResult")
            btn = self.driver.find_element(By.XPATH, "//button[text()='Try it']")
            self.driver.execute_script("arguments[0].click();", btn)
            self.driver.switch_to.default_content()

    def handle_multiple_windows(self):
        parent = self.driver.current_window_handle
        all_handles = self.driver.window_handles

        for handle in all_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                print("🪟 Switched to new window:", self.driver.title)
                time.sleep(2)
                self.driver.close()

        self.driver.switch_to.window(parent)
