#!/usr/bin/env python3
"""A simple flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class for flask app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index():
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
