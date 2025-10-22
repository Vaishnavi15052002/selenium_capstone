from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver(browser="chrome"):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(), options=ChromeOptions())
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(), options=FirefoxOptions())
    elif browser.lower() == "edge":
        driver = webdriver.Edge(service=EdgeService(), options=EdgeOptions())
    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
