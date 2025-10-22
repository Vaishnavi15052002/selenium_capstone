from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DemoBlazeSignup(BasePage):
    signup_btn_header = (By.ID, "signin2")
    username_input = (By.ID, "sign-username")
    password_input = (By.ID, "sign-password")
    signup_btn_modal = (By.XPATH, "//button[text()='Sign up']")

    def signup(self, username, password):
        self.click(self.signup_btn_header)
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        self.click(self.signup_btn_modal)
        self.handle_alert()
