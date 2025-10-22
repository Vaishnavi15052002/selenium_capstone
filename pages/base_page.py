from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def hover(self, locator):
        ActionChains(self.driver).move_to_element(self.wait.until(EC.visibility_of_element_located(locator))).perform()

    def scroll_down(self, pixels=500):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def scroll_up(self, pixels=500):
        self.driver.execute_script(f"window.scrollBy(0, -{pixels});")

    def handle_alert(self, accept=True):
        alert = self.wait.until(EC.alert_is_present())
        if accept:
            alert.accept()
        else:
            alert.dismiss()
