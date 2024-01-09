#!/usr/bin/env python3
"""A simple flask app"""


from flask import Flask, render_template, g, request
from flask_babel import Babel


class Config:
    """config class for flask app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get user id from request"""
    user = request.args.get('login_as')

    if user:
        try:
            user = int(user)
        except ValueError:
            pass
        else:
            user = users.get(user)
            if user:
                return user


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request():
    """handle before all other functions"""
    user = get_user()
    setattr(g, 'user', user)


def get_locale():
    """verifies users locale"""
    user_locale = request.args.get('locale')

    if user_locale is not None and user_locale in app.config["LANGUAGES"]:
        return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index():
    return render_template("5-index.html", user=getattr(g, 'user', None))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
