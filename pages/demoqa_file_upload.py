import os
import time
from selenium.webdriver.common.by import By

class DemoQAFileUpload:
    def __init__(self, driver):
        self.driver = driver
        self.upload_input = (By.ID, "uploadFile")

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def upload_file(self, file_path):
        file_input = self.driver.find_element(*self.upload_input)
        file_input.send_keys(file_path)
        time.sleep(2)

    def get_uploaded_file_name(self):
        return self.driver.find_element(By.ID, "uploadedFilePath").text
