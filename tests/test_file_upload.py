import os
import pytest
from utils.driver_factory import DriverFactory  # use DriverFactory for multiple browsers
from pages.demoqa_file_upload import DemoQAFileUpload


@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
def test_file_upload(browser_name):
    # Get driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    # Initialize page object
    page = DemoQAFileUpload(driver)
    page.open_url("https://demoqa.com/upload-download")

    # Prepare a dummy file for upload
    file_path = os.path.join(os.getcwd(), "sample_upload.txt")
    with open(file_path, "w") as f:
        f.write("This is a test file upload.")

    # Upload the file
    page.upload_file(file_path)
    uploaded_text = page.get_uploaded_file_name()

    # Assert file upload
    assert "sample_upload.txt" in uploaded_text, "File upload failed"

    # Quit the browser
    driver.quit()
