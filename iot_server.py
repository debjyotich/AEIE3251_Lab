# Experiment no. 3a
from flask import Flask, render_template
from flask_restful import reqparse

app = Flask(__name__)


# Experiment no. 3b
@app.route("/")
def home():
    return render_template("index.html")


# Experiment no. 3c
@app.route("/update", methods=["GET"])
def update():
    parser = reqparse.RequestParser()

    parser.add_argument("key", type=str)
    parser.add_argument("sensor_data", type=float)

    data_iot_board = parser.parse_args()

    if data_iot_board["key"] == "AABB":
        print(data_iot_board)
        return "200 OK"
    else:
        return "404"


if __name__ == "__main__":
    app.run(host="192.168.26.14")
