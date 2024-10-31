from ..db import db


class User(db.Model, UserMixin):
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    cartProducts = db.Column(db.String(80), nullable=False)
 
    # is_active = db.Column(db.Boolean(), default=True)