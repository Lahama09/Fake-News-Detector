        news = request.form["news"]

        # Transform input
        vect = vectorizer.transform([news])
        prediction = model.predict(vect)

        result = "Fake News ❌" if prediction[0] == "FAKE" else "Real News ✅"
        return render_template("index.html", prediction=result, news=news)

if __name__ == "__main__":
    app.run(debug=True)
