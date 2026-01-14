# Fake News Detector
A machine learning–powered web application that classifies news headlines and articles as FAKE or REAL, helping combat misinformation in digital media.

Built with Python (Scikit‑learn + NLP), Flask, and a responsive frontend (HTML, CSS, Bootstrap, JavaScript). 

🚀 Features
ML Model Integration: Trained using Scikit‑learn with NLP techniques (TF‑IDF vectorization, text preprocessing).

Real‑time Classification: Detects whether a headline/article is fake or real instantly.

Responsive UI: Built with HTML, CSS, Bootstrap, and JavaScript, including dark mode toggle.

API Integration: Connected with NewsAPI to fetch live headlines for classification.

Project Hygiene: Version control with Git/GitHub, model serialization, and modular Flask integration.


🛠️ Tech Stack
Languages: Python, JavaScript, HTML5, CSS3

Frameworks & Libraries: Flask, Scikit‑learn, Bootstrap, NLP (TF‑IDF, tokenization)

Tools: Git, GitHub, VS Code

APIs: NewsAPI


📂 Project Structure
Fake-News-Detector/
│
├── static/              # CSS, JS, images
├── templates/           # HTML templates
├── model/               # Serialized ML model files
├── app.py               # Flask backend
├── requirements.txt     # Dependencies
└── README.md            # Project documentation


⚙️ Installation & Setup
1. Clone the repository 
git clone https://github.com/Lahama09/Fake-News-Detector.git
cd Fake-News-Detector
2. Install dependencies
pip install -r requirements.txt
3. Run the flask app
python app.py
4. Open in browser  
Navigate to http://127.0.0.1:5000/


📊 Model Details
Algorithm: Logistic Regression / Naive Bayes (Scikit‑learn)

Features: TF‑IDF vectorization of text data

Dataset: News headlines/articles (preprocessed for training)

Accuracy: ~XX% (update with your benchmark results)


🌟 Future Enhancements
Deploy on Heroku / AWS / Azure for public access.

Add multi‑language support for global news detection.

Improve accuracy with deep learning models (LSTM, BERT).

Enhance UI with React.js  frontend.


👩‍💻 Author
Lahama Ghosh Dastidar

📧 lahama.gd.work@gmail.com

🔗 LinkedIn (https://www.linkedin.com/in/lahama-ghosh-dastidar-4b22b21b6/)

🔗 GitHub (https://github.com/Lahama09)