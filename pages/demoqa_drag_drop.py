from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DemoQADragDrop:
    def __init__(self, driver):
        self.driver = driver
        self.source = (By.ID, "draggable")
        self.target = (By.ID, "droppable")

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def perform_drag_and_drop(self):
        wait = WebDriverWait(self.driver, 10)
        source = wait.until(EC.visibility_of_element_located(self.source))
        target = wait.until(EC.visibility_of_element_located(self.target))

        # ✅ Use ActionChains offset drag — works with DemoQA
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).pause(0.5).move_to_element(target).pause(0.5).release().perform()

        time.sleep(1.5)  # wait for text to update

    def get_drop_text(self):
        return self.driver.find_element(*self.target).text
