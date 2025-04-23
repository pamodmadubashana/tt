from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
# Use environment variable for security

@app.route('/')
def home():
    return "Telegram Relay Server is running!"

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    chat_id = data.get("chat_id")
    text = data.get("text")

    if  not text:
        return jsonify({"error": "Missing 'text'"}), 400

    url = 'https://api.telegram.org/bot7407093168:AAGr2ASNpk4mAgMI_WfE01J2wJVyADIyTyk/sendMessage'
    payload = {
        'chat_id': 7859877609,
        'text': text
    }

    try:
        response = requests.post(url, json=payload)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

