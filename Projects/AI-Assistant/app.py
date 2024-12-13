from flask import Flask, render_template, request
from src.assistant import AIAssistant

app = Flask(__name__)
ai_assistant = AIAssistant()

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = ai_assistant.get_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
