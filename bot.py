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
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Fill out the form (adjust element names accordingly)
name_field = driver.find_element(By.NAME, "fname")
name_field.send_keys("John Doe")

email_field = driver.find_element(By.NAME, "lname")
email_field.send_keys("johndoe@example.com")

# Submit the form (if applicable)
email_field.send_keys(Keys.RETURN)

# Wait for 3 seconds before closing
time.sleep(3)
driver.quit()
