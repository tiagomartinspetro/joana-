from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ----------- UltraMsg Config -----------
ULTRAMSG_TOKEN = "SEU_TOKEN_AQUI"
ULTRAMSG_INSTANCE = "SEU_INSTANCE_ID"
ULTRAMSG_URL = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE}/messages/chat"

# ----------- Enviar mensagem -----------
def send_message(message, number):
    payload = {
        "token": ULTRAMSG_TOKEN,
        "to": number,
        "body": message
    }
    requests.post(ULTRAMSG_URL, data=payload)

# ----------- Webhook (mensagem recebida) -----------
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Mensagem recebida:", data)

    # número de quem enviou
    sender = data.get("from")

    # texto recebido
    text = data.get("body", "").lower()

    # resposta simples
    if "oi" in text or "olá" in text:
        send_message("Olá! Aqui é a Joana 😊 Como posso te ajudar hoje?", sender)
    else:
        send_message("Recebi sua mensagem! Já estou aqui para te ajudar 🌼", sender)

    return jsonify({"status": "received"}), 200

# ----------- Home -----------
@app.route('/', methods=['GET'])
def home():
    return "Joana WhatsApp Bot ativo!"

# ----------- Start -----------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
