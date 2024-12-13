from flask import Flask, render_template, request
from src.review import analyze_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    analysis = None
    if request.method == "POST":
        code = request.form["code"]
        analysis = analyze_code(code)
    return render_template("index.html", analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)
