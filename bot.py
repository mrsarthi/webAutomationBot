from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keeps the browser open
driver = webdriver.Chrome(options=options)

try:
    # Open the form page
    driver.get("http://127.0.0.1:5000/")
    time.sleep(2)  # Wait for the page to load

    # Fill the form
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.NAME, "email")
    message_input = driver.find_element(By.NAME, "message")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    name_input.send_keys("John Doe")
    email_input.send_keys("john@example.com")
    message_input.send_keys("This is an automated test.")
    submit_button.click()

    time.sleep(2)  # Wait for submission to complete

    # Take a screenshot to verify submission
    driver.save_screenshot("form_submission.png")

    print("✅ Form submitted successfully! Screenshot saved.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()  # Close the browser
