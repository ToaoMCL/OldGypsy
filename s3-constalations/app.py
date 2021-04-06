from flask import Flask, Response

app = Flask(__name__)

@app.route("/get/constalation", methods=["GET"])
def home():
    return Response("Taurus", mimetype='text/plain')


if __name__ == "__main__":
    app.run(port=5002, debug=True, host='0.0.0.0')