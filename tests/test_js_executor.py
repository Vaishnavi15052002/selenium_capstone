import pytest
from utils.driver_factory import DriverFactory  # use DriverFactory for multiple browsers
from pages.demoqa_js_executor import DemoQAJSExecutor


@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
def test_js_executor(browser_name):
    # Get driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    # Initialize page object
    page = DemoQAJSExecutor(driver)
    page.open_url("https://demoqa.com")

    # Perform actions using JavaScript
    page.scroll_and_highlight()
    page.generate_custom_alert("JavaScript executed successfully!")

    # Quit the browser
    driver.quit()
