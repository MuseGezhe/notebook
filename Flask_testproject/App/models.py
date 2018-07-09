from flask_login import UserMixin

from App.ext import db


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)
    pwd = db.Column(db.String(30))
    age = db.Column(db.Integer)
    pic = db.Column(db.String(300))

class Movie(db.Model):
    mid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(300))
    description = db.Column(db.String(300))
    online_time = db.Column(db.Date)