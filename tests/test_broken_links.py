import pytest
from utils.driver_factory import get_driver
from pages.demoqa_broken_links import DemoQABrokenLinks

def test_broken_links():
    driver = get_driver("chrome")
    page = DemoQABrokenLinks(driver)
    page.open_url("https://demoqa.com/links")

    broken_links = page.check_broken_links()
    if broken_links:
        print("Broken links found:")
        for link, code in broken_links:
            print(f"{link} - {code}")
    else:
        print("✅ No broken links found!")

    driver.quit()
