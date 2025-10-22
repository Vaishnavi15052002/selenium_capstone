import requests
from selenium.webdriver.common.by import By

class DemoQABrokenLinks:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def check_broken_links(self):
        links = self.driver.find_elements(By.TAG_NAME, "a")
        broken_links = []
        for link in links:
            href = link.get_attribute("href")
            if href:
                try:
                    response = requests.head(href, timeout=5)
                    if response.status_code >= 400:
                        broken_links.append((href, response.status_code))
                except Exception as e:
                    broken_links.append((href, str(e)))
        return broken_links
