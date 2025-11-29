from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)
    return jsonify({"status": "ok"})

@app.route('/', methods=['GET'])
def home():
    return "Joana WhatsApp Bot ativo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
