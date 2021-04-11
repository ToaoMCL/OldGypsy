from flask import Flask, Response, jsonify
from random import randrange

app = Flask(__name__)

constalations = [
    { "Aries": 1 },
    { "Taurus": 7 },
    { "Gemini": 6 },
    { "Cancer": 7 },
    { "Leo": 9 },
    { "Virgo": 6 },
    { "Libra": 3 },
    { "Scorpio": 4 },
    { "Sagittarius": 6 },
    { "Capricorn": 2 },
    { "Aquarius": 5 },
    { "Pisces": 3 }
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