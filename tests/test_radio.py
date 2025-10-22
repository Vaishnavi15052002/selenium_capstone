import pytest
from utils.driver_factory import get_driver
from pages.demoqa_radio import DemoQARadio

@pytest.mark.parametrize("option", ["yes", "impressive", "no"])
def test_radio(option):
    driver = get_driver("chrome")
    page = DemoQARadio(driver)
    page.open_url("https://demoqa.com/radio-button")
    page.select_radio(option)
    driver.quit()
