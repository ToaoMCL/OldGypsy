from flask import Flask, Response, jsonify
from random import randrange

app = Flask(__name__)

constalations = [
    { "JAmblA": 4 },
    { "A bipedal Bull": 2 },
    { "Water Bottle": 5 }  
    ]

def GetPosFromListOfDicts(list_of_dicts):
    return randrange(0, len(list_of_dicts))

@app.route("/get/constalation", methods=["GET"])
def home():
    constalation_pos = GetPosFromListOfDicts(constalations)
    constalation_key = list(constalations[constalation_pos])[0]
    response_data = { "constalation_name":constalation_key, "constalation_weight": constalations[constalation_pos][constalation_key] }
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(port=5002, debug=True, host='0.0.0.0')