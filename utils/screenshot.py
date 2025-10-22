import os
import datetime

def take_screenshot(driver, name_prefix="screenshot"):
    # Create a 'screenshots' folder inside project root
    folder = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Use timestamp to make filenames unique
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{name_prefix}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    driver.save_screenshot(filepath)
    print(f"📸 Screenshot saved: {filepath}")
    return filepath
