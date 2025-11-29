from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

INSTANCE_ID = "instance153047"
TOKEN = "2jl1sfhtu3kkvx4q"

# ---------------------------------------------------------
# FUNÇÃO PARA ENVIAR MENSAGENS PELO ULTRAMSG
# ---------------------------------------------------------
def send_message(message, to):
    url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"
    payload = { "token": TOKEN, "to": to, "body": message }
    try:
        response = requests.post(url, data=payload)
        print("UltraMsg:", response.text)
    except Exception as e:
        print("Erro UltraMsg:", e)


# ---------------------------------------------------------
# RESPOSTAS AUTOMÁTICAS DA JOANA
# ---------------------------------------------------------
def gerar_resposta(texto):
    texto = texto.lower()

    # Saudação inicial
    if texto in ["oi", "opa", "olá", "ola", "bom dia", "boa tarde", "boa noite", "menu", "iniciar"]:
        return (
            "Olá, meu nome é Joana de Souza, como posso te ajudar?\n\n"
            "Aqui estão as opções:\n"
            "1 - Buquês\n"
            "2 - Vasos plantados\n"
            "3 - Presentes e complementos\n"
            "4 - Entregas\n"
            "5 - Falar com atendimento humano"
        )

    # Opção 1 – Buquês
    if "1" == texto or "buqu" in texto:
        return (
            "Temos várias opções de buquês.\n\n"
            "🌻 Girassóis\n"
            "Temos girassóis em buquês e também em vasos plantados, o que você prefere? "
            "Posso te enviar as duas opções se você quiser.\n\n"
            "🌷 Rosas coloridas\n"
            "💐 Flores do campo\n\n"
            "Se quiser, posso enviar fotos e valores."
        )

    # Opção 2 – Vasos plantados
    if "2" == texto or "vaso" in texto:
        return (
            "Temos vasos plantados de diversas espécies:\n"
            "🌻 Girassol\n"
            "🌿 Plantas verdes\n"
            "🌸 Flores da época\n\n"
            "Posso enviar fotos e valores."
        )

    # Opção 3 – Presentes
    if "3" == texto or "presente" in texto or "complemento" in texto:
        return (
            "Temos presentes e complementos como:\n"
            "🎈 Balões\n"
            "🧸 Pelúcias\n"
            "🍫 Chocolates\n"
            "🎁 Cestas especiais\n\n"
            "Deseja ver opções?"
        )

    # Opção 4 – Entregas
    if "4" == texto or "entrega" in texto:
        return (
            "Realizamos entregas de segunda a sábado, das 9h às 18h.\n"
            "Podemos entregar em qualquer bairro de Petrópolis.\n\n"
            "Pode me informar o bairro para calcular?"
        )

    # Opção 5 – Humano
    if "5" == texto or "humano" in texto or "atendente" in texto:
        return (
            "Claro! Vou pedir para alguém da equipe continuar o atendimento por aqui. "
            "Só um instante."
        )

    # Girassol específico
    if "girass" in texto:
        return (
            "Temos girassóis em buquês e também em vasos plantados.\n"
            "Qual você prefere? Posso te enviar as duas opções."
        )

    # Mensagem padrão
    return (
        "Não encontrei essa opção.\n\n"
        "Digite:\n"
        "1 - Buquês\n"
        "2 - Vasos plantados\n"
        "3 - Presentes\n"
        "4 - Entregas\n"
        "5 - Falar com atendimento humano"
    )


# ---------------------------------------------------------
# WEBHOOK (RECEBE MENSAGENS DO WHATSAPP)
# ---------------------------------------------------------
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    sender = data.get("from")
    texto = data.get("body", "")

    resposta = gerar_resposta(texto)

    send_message(resposta, sender)

    return jsonify({"status": "ok"}), 200


# ---------------------------------------------------------
# ROTA DE TESTE
# ---------------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return "Joana está ativa!"


# ---------------------------------------------------------
# EXECUTAR LOCALMENTE
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
