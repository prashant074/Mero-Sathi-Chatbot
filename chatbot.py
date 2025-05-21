from flask import Flask, request, render_template, redirect, url_for
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

app = Flask(__name__)

# Globals to store chat session and history
chat = None
chat_history = []

def start_new_chat():
    global chat, chat_history
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat()
    chat_history = []

# Start first chat session
start_new_chat()

@app.route("/", methods=["GET", "POST"])
def index():
    global chat, chat_history
    if request.method == "POST":
        user_input = request.form.get("user_input")

        if user_input.lower() == "exit":
            return redirect(url_for("end_chat"))

        response = chat.send_message(user_input).text
        chat_history.append(("You", user_input))
        chat_history.append(("Mero Sathi", response))

    return render_template("index.html", chat_history=chat_history)

@app.route("/new_chat")
def new_chat():
    start_new_chat()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
