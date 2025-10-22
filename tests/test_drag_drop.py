import pytest
import time
from utils.driver_factory import get_driver
from pages.demoqa_drag_drop import DemoQADragDrop

def test_drag_and_drop():
    driver = get_driver("chrome")
    page = DemoQADragDrop(driver)
    page.open_url("https://demoqa.com/droppable")

    page.perform_drag_and_drop()

    # retry few times
    for _ in range(5):
        if page.get_drop_text() == "Dropped!":
            break
        time.sleep(0.5)

    assert page.get_drop_text() == "Dropped!", "Drag and drop failed"

    driver.quit()
