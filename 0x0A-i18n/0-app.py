#!/usr/bin/env python3
""" this module sets up Flask """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """ this method renders index.html template """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
