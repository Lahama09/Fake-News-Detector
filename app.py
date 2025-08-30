from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load the trained model + vectorizer
model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        news = request.form["news"]
        data = [news]
        vect = vectorizer.transform(data).toarray()
        prediction = model.predict(vect)

        result = "Fake News ❌" if prediction[0] == 0 else "Real News ✅"
        return render_template("index.html", prediction=result, news=news)

if __name__ == "__main__":
    app.run(debug=True)
