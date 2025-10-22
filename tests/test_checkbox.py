import pytest
from utils.driver_factory import DriverFactory
from pages.demoqa_checkbox import DemoQACheckbox


# Parametrize both browsers and checkbox options
@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
@pytest.mark.parametrize("option", ["notes", "commands"])
def test_checkboxes(browser_name, option):
    # Get the driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    # Initialize the page object
    page = DemoQACheckbox(driver)
    page.open_url("https://demoqa.com/checkbox")

    # Expand all checkboxes and select the required option
    page.expand_all_checkboxes()
    page.select_checkbox(option)

    driver.quit()
