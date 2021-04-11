from flask import Flask, Response, jsonify
from random import randrange
import json

app = Flask(__name__)

def GetRandomPosFromVariable(variable):
    return randrange(0, len(variable))

@app.route("/get/card", methods=["GET"])
def home():  
    with open("cards.json") as json_file:
        data = json_file.read()
    card_data = json.loads(data)
    card_pos = GetRandomPosFromVariable(card_data)

    keys = []  
    for key in card_data:
        keys.append(key)

    card_name = keys[card_pos]
    card_weight = card_data[keys[card_pos]]

    response_data = { "card_name":card_name, "card_weight":card_weight }

    return jsonify(response_data)



if __name__ == "__main__":
    app.run(port=5003, debug=True, host="0.0.0.0")