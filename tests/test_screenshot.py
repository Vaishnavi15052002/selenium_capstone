import pytest
from utils.driver_factory import get_driver
from utils.screenshot import take_screenshot

def test_screenshot_demo():
    driver = get_driver("chrome")
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

    # Take screenshot of homepage
    take_screenshot(driver, "demoblaze_home")

    driver.quit()
