import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load dataset
df = pd.read_csv("training_data.csv")

# Train ML model for message generation
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Message"])
y = range(len(df))

model = MultinomialNB()
model.fit(X, y)

# Generate a realistic message


def generate_message():
    sample_text = ["sample input"]  # Use a non-empty placeholder
    transformed_text = vectorizer.transform(sample_text)
    random_index = model.predict(transformed_text)[0]
    return df["Message"].iloc[random_index]

# Generate realistic names and emails from dataset


def generate_name():
    return random.choice(df["Name"].tolist())


def generate_email():
    return random.choice(df["Email"].tolist())


# Start Selenium WebDriver
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000")
time.sleep(2)

# Fill in the form using ML-generated data
driver.find_element(By.ID, "name").send_keys(generate_name())
driver.find_element(By.ID, "email").send_keys(generate_email())
driver.find_element(By.ID, "message").send_keys(generate_message())

# Submit form
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

# Screenshot to verify form submission
driver.save_screenshot("form_submission.png")

# Close browser
driver.quit()
