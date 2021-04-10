from flask import Flask
import requests
import os 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["WTF_CSRF_ENABLED"] = False
app.config["DEBUG"] = False
db = SQLAlchemy(app)

def Template_Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

db.create_all()
newent = Template_Table(name="new entry")
db.session.add(newent)
db.session.commit()

@app.route("/", methods=["GET"])
def home():
    card = requests.get("http://tarot-cards:5003/get/card")   
    constalation = requests.get("http://constilations:5002/get/constalation")
    premonition = requests.get("http://combination:5001/get/premonition/a/2/b/3")
    return constalation.text + "\n" + card.text + premonition.text


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")