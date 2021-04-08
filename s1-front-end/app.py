from flask import Flask
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    response = requests.get('http://oldgypsy_constilations_1:5002/get/constalation')
    card = requests.get('http://oldgypsy_tarot-cards_1:5003/get/card')
    return "Constalation " + response.text + "\n" + "Card " + card.text


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')