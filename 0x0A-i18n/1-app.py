#!/usr/bin/env python3
""" this module sets up Flask """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel()


@app.route('/', methods=['GET'])
def index():
    """ this method renders index.html template """
    return render_template('0-index.html')


class Config(object):
    """ this class configures available languages """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
