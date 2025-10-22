from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoQAMultipleWindows:
    def __init__(self, driver):
        self.driver = driver
        self.new_tab_button = (By.ID, "tabButton")
        self.new_window_button = (By.ID, "windowButton")

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def safe_click(self, locator):
        """Tries normal click first, then JavaScript click as fallback"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except Exception:
            # Scroll into view and use JS click
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def click_new_tab(self):
        self.safe_click(self.new_tab_button)

    def click_new_window(self):
        self.safe_click(self.new_window_button)

    def switch_to_new_window(self):
        handles = self.driver.window_handles
        parent = self.driver.current_window_handle
        for handle in handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                break

    def get_current_page_text(self):
        body = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return body.text

    def close_current_window(self):
        self.driver.close()

    def switch_back_to_parent(self, parent_handle):
        self.driver.switch_to.window(parent_handle)
