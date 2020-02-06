from flask import Flask
app = Flask(__name__)

@app.route('/mood')
def get_mood():
    return 'Hello, World!'

@app.route('/start_bot')
def start_bot():
    return 'Hello, World!'

@app.route('/channel')
def get_channel_data():
    return 'Hello, World!'