from flask import Flask, jsonify, render_template
import requests
import os 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["WTF_CSRF_ENABLED"] = False
app.config["DEBUG"] = False
db = SQLAlchemy(app)

class Fortune(db.Model):
    id                  = db.Column(db.Integer, primary_key=True)
    card_name           = db.Column(db.String(30))
    card_weight         = db.Column(db.Integer)
    constalation_name   = db.Column(db.String(30))
    constalation_weight = db.Column(db.Integer)
    luck                = db.Column(db.Float)
    fortune             = db.Column(db.String(300))



@app.route("/", methods=["GET"])
def home():
    card = requests.get("http://tarot-cards:5003/get/card")   
    constalation = requests.get("http://constilations:5002/get/constalation")
    data = card.json()
    data["constalation_name"] = constalation.json()["constalation_name"]
    data["constalation_weight"] = constalation.json()["constalation_weight"]
    premonition = requests.post("http://combination:5001/get/premonition", json=data)
    finished_prediction = premonition.json()
    fortune = ""
    if finished_prediction["luck"] > 10:
        fortune = "Good fortune awaits you"
    elif finished_prediction["luck"] > 5:
        fortune = "Your fortune bears the color beige"
    else:
        fortune = "Your fortune looks bleak"
    finished_prediction["fortune"] = fortune

    db.session.add(Fortune(card_name=finished_prediction["card_name"],card_weight=finished_prediction["card_weight"],constalation_name=finished_prediction["constalation_name"],constalation_weight=finished_prediction["constalation_weight"],luck=finished_prediction["luck"],fortune=finished_prediction["fortune"]))
    db.session.commit()

    return render_template("home.html", prediction=finished_prediction) #constalation.text + "\n" + card.text + premonition.text + "\n" + os.getenv("app_version")# + response_string

@app.route("/past", methods=["GET"])
def past_fortunes():
    predictions = []
    response = db.session.query(Fortune).all()
    for i in response:
        predictions.append(i.card_name + " " + str(i.card_weight) + " " + i.constalation_name + " " + str(i.constalation_weight) + " " + str(i.luck) + " " + i.fortune)
    return render_template("past.html", predictions=predictions)

if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")