import pytest
from utils.driver_factory import get_driver
from pages.demoblaze_login import DemoBlazeLogin

login_data = [
    {"username": "VaishnaviK123", "password": "Vaishu@123"}
]

@pytest.mark.parametrize("data", login_data)
def test_login_logout(data):
    driver = get_driver("chrome")
    login_page = DemoBlazeLogin(driver)
    login_page.open_url("https://www.demoblaze.com/")

    success = login_page.login(data['username'], data['password'])
    assert success, "Login failed — please check credentials or page state"

    login_page.logout()
    driver.quit()
