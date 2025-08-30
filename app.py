from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model + vectorizer (they were saved together in model.pkl)
with open("model/model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        news = request.form["news"]

        # Transform input
        vect = vectorizer.transform([news])
        prediction = model.predict(vect)

        result = "Fake News ❌" if prediction[0] == "FAKE" else "Real News ✅"
        return render_template("index.html", prediction=result, news=news)

if __name__ == "__main__":
    app.run(debug=True)
