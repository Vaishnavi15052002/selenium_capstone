import os
import csv
import pytest
from utils.driver_factory import DriverFactory  # use DriverFactory for multiple browsers
from pages.demoblaze_login import DemoBlazeLogin

# Step 1: Create folder and CSV file if they don't exist
folder_path = "data"
file_path = os.path.join(folder_path, "login_data.csv")

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(file_path):
    # Sample login data
    login_rows = [
        {"username": "VaishnaviK123", "password": "Vaishu@123"},
        {"username": "TestUser", "password": "Test@123"}
    ]
    # Write CSV
    with open(file_path, mode="w", newline="") as csvfile:
        fieldnames = ["username", "password"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(login_rows)


# Step 2: Function to read CSV
def get_login_data_from_csv(file_path):
    data_list = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append({"username": row["username"], "password": row["password"]})
    return data_list


# Step 3: Read CSV data
login_data = get_login_data_from_csv(file_path)


# Step 4: Pytest test using CSV data on multiple browsers
@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
@pytest.mark.parametrize("data", login_data)
def test_login_logout(browser_name, data):
    # Get driver for the current browser
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)

    login_page = DemoBlazeLogin(driver)
    login_page.open_url("https://www.demoblaze.com/")

    success = login_page.login(data['username'], data['password'])
    assert success, f"Login failed for user {data['username']}"

    login_page.logout()
    driver.quit()
