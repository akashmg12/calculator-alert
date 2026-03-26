from flask import Flask
import requests

app = Flask(__name__)

TOKEN = "8249369744:AAHFLH25QQeahpI3At-0ZHcc5z_UwZ1Q0-A"
CHAT_ID = "7547727012"

@app.route('/alert', methods=['GET', 'POST'])
def alert():
    message = "Call me now"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    return "Alert Sent!"

app.run()