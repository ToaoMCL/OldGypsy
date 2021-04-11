from flask import Flask, Response, request, jsonify
from random import randrange

app = Flask(__name__)

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

@app.route("/get/premonition", methods=["POST"])
def home():
    data = request.json
    luck = data["card_weight"] + data["constalation_weight"]

    for i in range(0,10):
        clamp(luck * random.uniform(0.5, 1.5),0 , 20)
    data["luck"] = luck 
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5001, debug=True, host='0.0.0.0')