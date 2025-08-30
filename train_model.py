import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
import pickle, os

# Load dataset
df = pd.read_csv("fake_news_dataset.csv")

# Features & labels
x = df["text"]
y = df["label"]

# Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Vectorization
tfidf = TfidfVectorizer(stop_words="english", max_df=0.7)
x_train_tfidf = tfidf.fit_transform(x_train)
x_test_tfidf = tfidf.transform(x_test)

# Train classifier
classifier = PassiveAggressiveClassifier(max_iter=50)
classifier.fit(x_train_tfidf, y_train)

# Test accuracy
y_pred = classifier.predict(x_test_tfidf)
acc = accuracy_score(y_test, y_pred) * 100
print(f"Model Accuracy: {acc:.2f}%")

# ✅ Save both vectorizer and model
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump((tfidf, classifier), f)
