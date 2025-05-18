from flask import Flask
import threading
from Extractor import __main__  # Ensure this runs the bot

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from john wick'

def run_bot():
    __main__.main()  # Or whatever the bot start function is called

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=5000)