import pandas as pd
import os

# Update this path to where your dataset was downloaded
dataset_path = r"C:\Users\hp\.cache\kagglehub\datasets\clmentbisaillon\fake-and-real-news-dataset\versions\1"

# Load both files
fake = pd.read_csv(os.path.join(dataset_path, "Fake.csv"))
true = pd.read_csv(os.path.join(dataset_path, "True.csv"))

# Add labels: 0 = Fake, 1 = Real
fake["label"] = 0
true["label"] = 1

# Combine into one dataset
data = pd.concat([fake, true], axis=0).sample(frac=1, random_state=42).reset_index(drop=True)

# Keep only the columns we need
data = data[["text", "label"]]

# Save as fake_news_dataset.csv inside project folder
data.to_csv("fake_news_dataset.csv", index=False)

print("Merged dataset saved as fake_news_dataset.csv")
