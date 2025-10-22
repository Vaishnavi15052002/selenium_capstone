import pytest
from utils.driver_factory import get_driver
from pages.demoqa_js_executor import DemoQAJSExecutor

def test_js_executor():
    driver = get_driver("chrome")
    page = DemoQAJSExecutor(driver)
    page.open_url("https://demoqa.com")
    page.scroll_and_highlight()
    page.generate_custom_alert("JavaScript executed successfully!")
    driver.quit()
