import pytest
from utils.driver_factory import DriverFactory
from pages.demoqa_radio import DemoQARadio

@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
@pytest.mark.parametrize("option", ["yes", "impressive", "no"])
def test_radio(browser_name, option):
    # Get driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    page = DemoQARadio(driver)
    page.open_url("https://demoqa.com/radio-button")
    page.select_radio(option)

    driver.quit()
