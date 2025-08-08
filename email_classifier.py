
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
from flask import Flask,request,render_template

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    y = [ps.stem(i) for i in y]
    return " ".join(y)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        email_text = request.form['email_text']
        transformed_text = transform_text(email_text)
        vector_input = vectorizer.transform([transformed_text])
        prediction = model.predict(vector_input)[0]
        
        if prediction == 1:
            result = "This is a spam email."
        else:
            result = "This is a legitimate email."

        return render_template('index.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
