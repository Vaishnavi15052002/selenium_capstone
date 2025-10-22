import pytest
import time
from utils.driver_factory import DriverFactory
from pages.demoqa_drag_drop import DemoQADragDrop


@pytest.mark.parametrize("browser_name", ["chrome"])
def test_drag_and_drop(browser_name):
    # Get the driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    # Initialize the page object
    page = DemoQADragDrop(driver)
    page.open_url("https://demoqa.com/droppable")

    # Perform drag and drop
    page.perform_drag_and_drop()

    # Retry a few times to ensure the drop action was successful
    for _ in range(5):
        if page.get_drop_text() == "Dropped!":
            break
        time.sleep(0.5)

    # Assert that drag and drop was successful
    assert page.get_drop_text() == "Dropped!", "Drag and drop failed"

    driver.quit()
