from ..db import db

class Products(db.Model, UserMixin):
    productID = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(20), unique=True, nullable=False)
    productImage = db.Column(db.String(80), nullable=False)
    productPrice = db.Column(db.String(80), nullable=False)
    productDesc = db.Column(db.String(80), nullable=False)
    # is_active = db.Column(db.Boolean(), default=True)