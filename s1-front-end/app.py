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

class Predictions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
'''
response_string = ""
response = db.session.query(Template_Table).all()
for i in response:
    response_string = response_string + str(i.id) + "," + i.name + "\n"
    
'''

@app.route("/", methods=["GET"])
def home():
    card = requests.get("http://tarot-cards:5003/get/card")   
    constalation = requests.get("http://constilations:5002/get/constalation")
    result = card.text
   # premonition = requests.post("http://combination:5001/get/premonition/a/2/b/3", json=)
    return result #constalation.text + "\n" + card.text + premonition.text + "\n" + os.getenv("app_version")# + response_string


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")