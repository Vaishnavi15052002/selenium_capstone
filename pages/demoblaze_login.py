from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DemoBlazeLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.login_link = (By.ID, "login2")
        self.username_field = (By.ID, "loginusername")
        self.password_field = (By.ID, "loginpassword")
        self.login_button = (By.XPATH, "//button[text()='Log in']")
        self.logout_link = (By.ID, "logout2")
        self.close_button = (By.XPATH, "//button[text()='Close']")

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, username, password):
        # Click login link
        self.wait.until(EC.element_to_be_clickable(self.login_link)).click()
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

        # Wait a bit to check if alert appears
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(f"⚠️ Alert appeared during login: {alert.text}")
            alert.accept()
            return False
        except:
            print("✅ Login successful — no alert appeared.")

        # Wait for logout button (only visible when login succeeds)
        try:
            self.wait.until(EC.visibility_of_element_located(self.logout_link))
            print("✅ Login verified — logout link visible.")
            return True
        except:
            print("❌ Login failed — logout link not visible.")
            return False

    def logout(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()
            print("✅ Logged out successfully.")
        except:
            print("⚠️ Logout link not found or already logged out.")
