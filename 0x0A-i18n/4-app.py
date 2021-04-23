#!/usr/bin/env python3
""" this module sets up Flask """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ this class configures available languages """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index():
    """ this method renders index.html template """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """ this method determines match for supported languages """
    arg_locale = request.args.get('locale')
    if arg_locale and arg_locale in Config.LANGUAGES:
        return arg_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
