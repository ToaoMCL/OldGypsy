from flask import Flask, Response, request, jsonify

app = Flask(__name__)
  

@app.route("/get/premonition", methods=["POST"])
def home():
    card = request.json
    return card["card_name"]


if __name__ == "__main__":
    app.run(port=5001, debug=True, host='0.0.0.0')