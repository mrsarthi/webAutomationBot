import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

df = pd.read_csv("training_data.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Message"])
y = range(len(df))

model = MultinomialNB()
model.fit(X, y)


def generate_message():
    sample_text = ["sample input"]
    transformed_text = vectorizer.transform(sample_text)
    random_index = model.predict(transformed_text)[0]
    return df["Message"].iloc[random_index]


def generate_name():
    return random.choice(df["Name"].tolist())


def generate_email():
    return random.choice(df["Email"].tolist())


driver = webdriver.Chrome()
driver.get("https://lavendergalliform.onpella.app/")
time.sleep(2)

driver.find_element(By.ID, "name").send_keys(generate_name())
driver.find_element(By.ID, "email").send_keys(generate_email())
driver.find_element(By.ID, "message").send_keys(generate_message())

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

# driver.save_screenshot("form_submission.png")

driver.quit()
