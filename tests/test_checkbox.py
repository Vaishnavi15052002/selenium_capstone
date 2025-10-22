import pytest
from utils.driver_factory import get_driver
from pages.demoqa_checkbox import DemoQACheckbox

@pytest.mark.parametrize("option", ["notes", "commands"])
def test_checkboxes(option):
    driver = get_driver("chrome")
    page = DemoQACheckbox(driver)
    page.open_url("https://demoqa.com/checkbox")
    page.expand_all_checkboxes()
    page.select_checkbox(option)
    driver.quit()
