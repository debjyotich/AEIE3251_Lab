# Experiment no. 3a
from flask import Flask, render_template

app = Flask(__name__)


# Experiment no. 3b
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="192.168.26.13")
