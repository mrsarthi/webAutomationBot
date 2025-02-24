import pandas as pd
from faker import Faker

fake = Faker()
data = []

for _ in range(1000):
    name = fake.name()
    email = fake.email()
    message = fake.sentence()
    data.append([name, email, message])

df = pd.DataFrame(data, columns=["Name", "Email", "Message"])
df.to_csv("training_data.csv", index=False)

print("Dataset saved as training_data.csv")
