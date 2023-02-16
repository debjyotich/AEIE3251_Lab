# Experiment no. 3a
from flask import Flask, render_template
from flask_restful import reqparse
import datetime

app = Flask(__name__)


# Experiment no. 3b
@app.route("/")
def home():
    return render_template("index.html")


# Experiment no. 3c
@app.route("/update", methods=["GET"])
def update():
    parser = reqparse.RequestParser()

    parser.add_argument("api_key", type=str)
    parser.add_argument("sensor_data", type=float)

    data = parser.parse_args()
    data['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(data)

    return "200"


@app.route("/feed", methods=["GET"])
def feed():
    parser = reqparse.RequestParser()

    parser.add_argument("api_key", type=str)

    data = parser.parse_args()


    print(data)

    return "200"


if __name__ == "__main__":
    app.run(host="192.168.26.15")
