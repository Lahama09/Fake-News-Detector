from flask import Flask, request, jsonify, render_template
import pickle
import requests
app = Flask(__name__, template_folder=".")

API_KEY = "e9e9679fe3dc429ab8784f0793371dcb"

# Load model + vectorizer
with open("model/model.pkl", "rb") as f:
    tfidf, classifier = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    news = data.get("text", "")
    if not news:
        return jsonify({"prediction": "UNKNOWN"})
    
    vect = tfidf.transform([news])
    prediction = classifier.predict(vect)[0]
    result = "FAKE" if prediction == 0 else "REAL"
    return jsonify({"prediction": result})

@app.route("/get_news", methods=["GET"])
def get_news():
    query = request.args.get("q", "bitcoin")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    articles = []
    for a in data.get("articles", []):
        text = a.get("title", "")
        vect = tfidf.transform([text])
        prediction = classifier.predict(vect)[0]
        result = "FAKE" if prediction == 0 else "REAL"
        articles.append({
            "title": text,
            "url": a.get("url", ""),
            "prediction": result
        })
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)