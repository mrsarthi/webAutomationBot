from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://amethystmosquito.onpella.app/")
    time.sleep(2)

    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.NAME, "email")
    message_input = driver.find_element(By.NAME, "message")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    name_input.send_keys("John Doe")
    email_input.send_keys("john@example.com")
    message_input.send_keys("This is an automated test.")

    submit_button.click()

    time.sleep(3)
    # driver.save_screenshot("form_submission.png")

    print("✅ Form submitted successfully! Screenshot saved.")


except Exception as e:
    print(f"❌ Error: {e}")

finally:
    driver.quit()
