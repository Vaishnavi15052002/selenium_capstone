import pytest
from utils.driver_factory import DriverFactory
from pages.demoqa_broken_links import DemoQABrokenLinks
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
def test_broken_links(browser_name):
    # Get the driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    # Initialize the page object
    page = DemoQABrokenLinks(driver)
    page.open_url("https://demoqa.com/links")

    # Check broken links
    broken_links = page.check_broken_links()

    if broken_links:
        print(f"Broken links found in {browser_name}:")
        for link, code in broken_links:
            print(f"{link} - {code}")
    else:
        print(f"✅ No broken links found in {browser_name}!")

    driver.quit()
