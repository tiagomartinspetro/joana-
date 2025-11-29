from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

INSTANCE_ID = "instance153047"
TOKEN = "2jl1sfhtu3kkvx4q"

# ---------------------------------------------------------
# FUNÇÃO PARA ENVIAR MENSAGEM PELO ULTRAMSG
# ---------------------------------------------------------
def send_message(message, to):
    url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"
    
    payload = {
        "token": TOKEN,
        "to": to,
        "body": message
    }

    response = requests.post(url, data=payload)
    print("Resposta UltraMsg
