📧 Email Spam Classifier
A simple Flask web application that classifies emails as Spam or Ham (not spam) using Machine Learning.

🚀 Features
🧠 Machine Learning Model trained on email datasets.

🌐 Flask Web App for easy interaction.

🎨 Modern UI with CSS styling.

📜 Preprocessing Pipeline for tokenization, stopword removal, and stemming.

🛠️ Tech Stack
Python

Flask

NLTK (Natural Language Processing)

Scikit-learn

Pickle (Model & Vectorizer storage)

HTML / CSS for UI

📂 Project Structure
csharp
Copy
Edit
email_spam_classifier/
│
├── static/
│   └── index.css               # Stylesheet
├── templates/
│   └── index.html              # Frontend template
├── model.pkl                   # Trained ML model
├── vectorizer.pkl              # TF-IDF Vectorizer
├── app.py                      # Flask app
├── README.md                   # Documentation
└── requirements.txt            # Python dependencies
⚙️ Installation & Setup
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/email_spam_classifier.git
cd email_spam_classifier
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app

bash
Copy
Edit
python app.py
Open in browser
Go to http://127.0.0.1:5000/

🧠 Model Training
The model is trained using TF-IDF Vectorization and Logistic Regression.

Preprocessing steps include:

Lowercasing text

Removing punctuation & stopwords

Tokenization

	Model	Accuracy	Precision
10	XGBoost	0.974855	0.961240
8	Extra Trees	0.973888	0.991667
1	SVM (Sigmoid)	0.971954	0.939394
5	Random Forest	0.970019	0.991379
2	Multinomial NB	0.961315	0.990654
7	Bagging	0.961315	0.877698
9	Gradient Boosting	0.950677	0.951923
0	Logistic Regression	0.943907	0.865546
3	Decision Tree	0.935203	0.814516
6	AdaBoost	0.914894	0.787879
4	KNN	0.896518	1.000000
Stemming

📊 Example Outputs
Email Text	Prediction
"You won $1000! Click here to claim now!"	Spam
"Let's meet for lunch tomorrow at 1 PM"	Ham
