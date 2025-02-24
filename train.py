import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

df = pd.read_csv("training_data.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Message"])
y = list(range(len(df)))

model = MultinomialNB()
model.fit(X, y)


def generate_message():
    sample_text = ["This is a sample input"]
    transformed_text = vectorizer.transform(sample_text)
    random_index = model.predict(transformed_text)[0]
    return df["Message"].iloc[random_index]


print("Generated Message:", generate_message())
