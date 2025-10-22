import pytest
from utils.driver_factory import get_driver
from pages.demoblaze_signup import DemoBlazeSignup

signup_data = [
    {"username": "VaishnaviK123", "password": "Vaishu@123"},
]

@pytest.mark.parametrize("data", signup_data)
def test_signup(data):
    driver = get_driver("chrome")
    signup_page = DemoBlazeSignup(driver)
    signup_page.open_url("https://www.demoblaze.com/")
    signup_page.signup(data['username'], data['password'])
    driver.quit()
