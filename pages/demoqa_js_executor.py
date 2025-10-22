import time
from selenium.webdriver.common.by import By

class DemoQAJSExecutor:
    def __init__(self, driver):
        self.driver = driver
        self.card_element = (By.XPATH, "//h5[text()='Elements']")

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def scroll_and_highlight(self):
        element = self.driver.find_element(*self.card_element)
        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Highlight element
        self.driver.execute_script("arguments[0].style.border='3px solid red';", element)
        time.sleep(2)

    def generate_custom_alert(self, message):
        self.driver.execute_script(f"alert('{message}')")
        time.sleep(2)
        self.driver.switch_to.alert.accept()
