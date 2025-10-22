import pytest
import time
from utils.driver_factory import get_driver
from pages.demoqa_multiple_windows import DemoQAMultipleWindows

def test_multiple_windows():
    driver = get_driver("chrome")
    page = DemoQAMultipleWindows(driver)
    page.open_url("https://demoqa.com/browser-windows")

    page.click_new_tab()
    time.sleep(2)
    page.handle_multiple_windows()

    assert len(driver.window_handles) == 1, "❌ Multiple windows not handled properly"
    print("✅ Multiple windows handled successfully")

    driver.quit()
