#配置第3方库-插件
from flask_bootstrap import Bootstrap
from flask_cache import Cache

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
lm = LoginManager()

cache = Cache(config={
    "CACHE_TYPE" : "redis",
    "CACHE_KEY_PREFIX" : "CA-",
})


def init_ext(app):
    db.init_app(app)
    Session(app=app)
    migrate.init_app(app=app,db=db)
    Bootstrap(app=app)
    cache.init_app(app=app)
    lm.init_app(app=app)