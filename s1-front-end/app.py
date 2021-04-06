from flask import Flask
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    response = requests.get('http://oldgypsy_constilations_1:5002/get/constalation')
    return "Constalation" + response.text


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')