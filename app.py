from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)