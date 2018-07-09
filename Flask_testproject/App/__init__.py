from flask import Flask

from App import settings
from App.ext import init_ext
from App.views import init_blue


def create_app(evnname):
    app = Flask(__name__)
    app.config.from_object(settings.config.get(evnname or "default"))
    init_ext(app=app)
    init_blue(app=app)
    return app