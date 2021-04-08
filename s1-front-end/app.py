from flask import Flask
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    response = requests.get("http://oldgypsy_constilations_1:5002/get/constalation")
    card = requests.get("http://oldgypsy_tarot-cards_1:5003/get/card")   
    premonition = requests.get("http://oldgypsy_combination_1:5001/get/premonition/a/2/b/3")
    return response.text + "\n" + card.text + premonition.text


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")