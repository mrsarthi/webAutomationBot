from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Automatically download and setup the correct WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a sample form (replace with any actual form URL)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScxfFwR8U2buJ8nwGQdoJmUi0--YL8bxkGMUbk8lrREbTgx2g/viewform?usp=header")

# Fill out the form (adjust element names accordingly)
name_field = driver.find_element(By.NAME, "entry.2005620554")
name_field.send_keys("John Doe")

email_field = driver.find_element(By.NAME, "entry.1045781291")
email_field.send_keys("johndoe@example.com")

email_field = driver.find_element(By.NAME, "entry.1166974658")
email_field.send_keys("johndoe@example.com")

email_field = driver.find_element(By.NAME, "entry.839337160")
email_field.send_keys("johndoe@example.com")

submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit_button.click()


# Wait for 3 seconds before closing
# time.sleep(3)
input("Press Enter to close the browser...")

driver.quit()
