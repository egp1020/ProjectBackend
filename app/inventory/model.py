from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

class Inventory(db.Model):
    __tablename__="inventory"
    id = db.Column(db.Integer, primary_key=True)
    product = db.relationship('Product', backref='inventory', lazy=True, uselist=False)
    stock = db.Column(db.Integer)
    date_created = db.Column( db.DateTime, nullable=False)

    def __init__(self, product, stock):
        self.product = product
        self.stock = stock
        self.date_created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")