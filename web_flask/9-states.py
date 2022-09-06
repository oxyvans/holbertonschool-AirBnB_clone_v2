#!/usr/bin/python3
""" TASK 10"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tdow(self):
    """teardown"""
    storage.close()


@app.route("/states", strict_slashes=False)
def stateslist():
    """displays"""
    List_s = storage.all(State).values()
    List_s = sorted(List_s, key=lambda k: k.name)
    return render_template("7-states_list.html", List_s=List_s)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
