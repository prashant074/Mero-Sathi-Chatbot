# Mero Sathi

A simple web-based chatbot powered by Google Gemini, built with Flask.

## Features

- Friendly web UI for chatting with "Mero Sathi"
- Remembers chat history during the session
- Option to start a new chat
- Styled with custom CSS

## Setup

1. **Clone the repository** and navigate to the project folder.

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   - Create a `.env` file in the project root with your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. **Run the app:**
   ```sh
   python chatbot.py
   ```

5. **Open your browser** and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

```
.
├── chatbot.py
├── requirements.txt
├── .env
├── static/
│   ├── logo.png
│   └── css/
│       └── style.css
└── templates/
    └── index.html
```

## Notes

- Requires Python 3.7+
- Make sure your API key is valid and has access to Gemini
- For development, `debug=True` is enabled in Flask

---

Made with ❤️ for learning and fun!
