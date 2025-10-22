from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage


class DemoBlazeCart(BasePage):

    # Locators
    cart_link = (By.ID, "cartur")
    place_order_btn = (By.XPATH, "//button[text()='Place Order']")
    name_input = (By.ID, "name")
    country_input = (By.ID, "country")
    city_input = (By.ID, "city")
    card_input = (By.ID, "card")
    month_input = (By.ID, "month")
    year_input = (By.ID, "year")
    purchase_btn = (By.XPATH, "//button[text()='Purchase']")

    def add_product_to_cart(self, product_name):
        wait = WebDriverWait(self.driver, 10)

        # Wait until login modal disappears (if present)
        login_modal = (By.ID, "logInModal")
        try:
            wait.until(EC.invisibility_of_element_located(login_modal))
        except:
            pass  # ignore if modal already gone

        # Wait for product link to be clickable

