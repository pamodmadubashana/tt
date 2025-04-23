from flask import Flask, request
import requests

app = Flask(__name__)
TOKEN = "your_bot_token"

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    res = requests.post(
        f'https://api.telegram.org/bot7407093168:AAGr2ASNpk4mAgMI_WfE01J2wJVyADIyTyk/sendMessage',
        json={
            'chat_id': 7859877609,
            'text': data['text']
        }
    )
    return res.json()

if __name__ == '__main__':
    app.run()
