import pytest
from utils.driver_factory import DriverFactory
from pages.demoqa_multiple_windows import DemoQAMultipleWindows
import time


@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
def test_multiple_windows(browser_name):
    # Get driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    page = DemoQAMultipleWindows(driver)
    page.open_url("https://demoqa.com/browser-windows")

    parent_handle = driver.current_window_handle

    # ✅ Click to open a new tab
    page.click_new_tab()
    page.switch_to_new_window()

    # ✅ Verify content in new tab
    text = page.get_current_page_text()
    assert "This is a sample page" in text, "Text not found in new tab!"

    # ✅ Close new tab and switch back
    page.close_current_window()
    page.switch_back_to_parent(parent_handle)

    # ✅ Optional: click new window and check again
    page.click_new_window()
    page.switch_to_new_window()
    text2 = page.get_current_page_text()
    assert "This is a sample page" in text2, "Text not found in new window!"

    driver.quit()
