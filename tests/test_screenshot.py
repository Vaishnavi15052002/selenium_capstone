import pytest
from utils.driver_factory import DriverFactory
from utils.screenshot import take_screenshot

@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
def test_screenshot_demo(browser_name):
    # Get driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

    # Take screenshot of homepage
    take_screenshot(driver, "demoblaze_home")

    driver.quit()
