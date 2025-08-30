import pickle

# Load the saved model
with open("model/model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

# Function to check if news is fake or real
def predict_news(news_text):
    # Transform input using the saved vectorizer
    transformed_text = vectorizer.transform([news_text])
    prediction = model.predict(transformed_text)[0]

    if prediction == 1:   # Assuming 1 = REAL, 0 = FAKE (based on your dataset)
        return "✅ This news seems REAL."
    else:
        return "❌ This news seems FAKE."

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a news text: ")
    result = predict_news(user_input)
    print(result)
