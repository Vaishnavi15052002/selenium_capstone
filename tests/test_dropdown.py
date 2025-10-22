import pytest
from utils.driver_factory import DriverFactory  # use DriverFactory to get all browsers
from pages.demoqa_dropdown import DemoQADropdown


# Parametrize both browsers and dropdown options
@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
@pytest.mark.parametrize("option", ["Red", "Green", "Blue"])
def test_dropdown(browser_name, option):
    # Get driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    # Initialize page object
    page = DemoQADropdown(driver)
    page.open_url("https://demoqa.com/select-menu")

    # Select dropdown option
    page.select_option(option)

    # Quit the browser
    driver.quit()
