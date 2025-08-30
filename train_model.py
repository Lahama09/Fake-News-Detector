# train_model.py
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1. Load dataset
# Replace this with your dataset CSV file
df = pd.read_csv("fake_news_dataset.csv")  
X = df["text"]
y = df["label"]

# 2. Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# 3. Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# 4. Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Save model and vectorizer
with open("model/fake_news_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved in 'model/' folder")
