from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/")

driver.find_element(By.NAME, "name").send_keys("John Doe")
driver.find_element(By.NAME, "email").send_keys("john@example.com")
driver.find_element(By.NAME, "message").send_keys("This is an automated test.")

driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(2)

driver.save_screenshot("form_submission.png")

driver.quit()
