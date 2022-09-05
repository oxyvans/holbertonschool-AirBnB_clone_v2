#!/usr/bin/python3
"""task 2"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """say hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """c is fun"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
