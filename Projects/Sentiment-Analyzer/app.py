from flask import Flask, render_template, request
from src.sentiment_analyzer import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
