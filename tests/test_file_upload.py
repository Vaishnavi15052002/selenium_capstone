import os
import pytest
from utils.driver_factory import get_driver
from pages.demoqa_file_upload import DemoQAFileUpload

def test_file_upload():
    driver = get_driver("chrome")
    page = DemoQAFileUpload(driver)
    page.open_url("https://demoqa.com/upload-download")

    # Prepare a dummy file for upload
    file_path = os.path.join(os.getcwd(), "sample_upload.txt")
    with open(file_path, "w") as f:
        f.write("This is a test file upload.")

    page.upload_file(file_path)
    uploaded_text = page.get_uploaded_file_name()

    assert "sample_upload.txt" in uploaded_text, "File upload failed"
    driver.quit()
