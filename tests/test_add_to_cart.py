import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_factory import DriverFactory  # import your factory


@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
def test_add_to_cart(browser_name):
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.demoblaze.com/")

    # Click on Samsung Galaxy S6
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6"))).click()

    # Click 'Add to cart'
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))).click()

    # Handle alert
    alert = wait.until(EC.alert_is_present())
    alert.accept()

    # Go to cart
    wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()

    # Verify item in cart
    product = wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'Samsung galaxy s6')]")))
    assert product.is_displayed(), "Product not found in cart!"

    driver.quit()
