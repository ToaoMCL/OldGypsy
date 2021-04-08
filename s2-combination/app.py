from flask import Flask, Response, request, jsonify

app = Flask(__name__)
  

@app.route("/get/premonition/<string:card>/<int:card_weight>/<string:constalation>/<string:constalation_weight>", methods=["GET"])
def home(card, card_weight, constalation, constalation_weight):
    
    return jsonify({card:card_weight}, {constalation:constalation_weight})


if __name__ == "__main__":
    app.run(port=5001, debug=True, host='0.0.0.0')