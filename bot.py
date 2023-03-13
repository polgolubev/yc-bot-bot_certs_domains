import os
import requests
import json
from datetime import datetime, timedelta

DAY_EXPIRIEN_ALERT = 8
PREMSG = f"{os.environ['PREMSG']}"

def send_message(text):
    url = f"https://api.telegram.org/bot%s/sendMessage" %os.environ['BOT_TOKEN']
    data = {"chat_id": os.environ['CHAT_ID'], "parse_mode": "HTML", "text": text}
    r = requests.post(url, data=data)
    return r

def handler(event, context):
    with open("data.json","r") as f:
        data = json.load(f)
        for item in data:
            for element in data[item]:
                count_day = (datetime.strptime(element["date_expiried"], "%d.%m.%Y") - datetime.now()).days
                if count_day < DAY_EXPIRIEN_ALERT:
                    send_message(f'{PREMSG}\n<b>{element["type"]} {element["name"]} истекает {element["date_expiried"]}</b> (Дней до окончания действия - {count_day}).')
    return {
        'statusCode': 200,
    }
