import pytest
from utils.driver_factory import get_driver
from pages.demoqa_dropdown import DemoQADropdown

@pytest.mark.parametrize("option", ["Red", "Green", "Blue"])
def test_dropdown(option):
    driver = get_driver("chrome")
    page = DemoQADropdown(driver)
    page.open_url("https://demoqa.com/select-menu")
    page.select_option(option)
    driver.quit()
