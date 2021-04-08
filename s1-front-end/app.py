from flask import Flask
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    card = requests.get("http://tarot-cards:5003/get/card")   
    constalation = requests.get("http://constilations:5002/get/constalation")
    premonition = requests.get("http://combination:5001/get/premonition/a/2/b/3")
    return constalation.text + "\n" + card.text #+ premonition.text


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")