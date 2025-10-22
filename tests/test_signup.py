import os
import csv
import pytest
from utils.driver_factory import DriverFactory
from pages.demoblaze_signup import DemoBlazeSignup

# Step 1: Create folder and CSV file if they don't exist
folder_path = "data"
file_path = os.path.join(folder_path, "signup_data.csv")

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(file_path):
    # Sample signup data
    signup_rows = [
        {"username": "VaishnaviK123", "password": "Vaishu@123"},
        {"username": "TestUser1", "password": "Test@123"}
    ]
    # Write CSV
    with open(file_path, mode="w", newline="") as csvfile:
        fieldnames = ["username", "password"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(signup_rows)

# Step 2: Function to read CSV
def get_signup_data_from_csv(file_path):
    data_list = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append({"username": row["username"], "password": row["password"]})
    return data_list

# Step 3: Read CSV data
signup_data = get_signup_data_from_csv(file_path)

# Step 4: Pytest test using CSV data on multiple browsers
@pytest.mark.parametrize("browser_name", ["chrome", "edge"])
@pytest.mark.parametrize("data", signup_data)
def test_signup(browser_name, data):
    driver = DriverFactory.get_driver(browser_name=browser_name, headless=False)
    signup_page = DemoBlazeSignup(driver)
    signup_page.open_url("https://www.demoblaze.com/")
    signup_page.signup(data['username'], data['password'])
    driver.quit()
