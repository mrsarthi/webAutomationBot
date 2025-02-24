import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load dataset
df = pd.read_csv("training_data.csv")

# Train model for message generation
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Message"])  # Convert messages to TF-IDF
y = list(range(len(df)))  # Dummy labels

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, y)


def generate_message():
    sample_text = ["This is a sample input"]  # Provide a placeholder input
    transformed_text = vectorizer.transform(sample_text)  # Convert to TF-IDF
    random_index = model.predict(transformed_text)[0]  # Predict index
    return df["Message"].iloc[random_index]


print("Generated Message:", generate_message())
