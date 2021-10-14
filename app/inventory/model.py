from app import db
from flask_sqlalchemy import SQLAlchemy

class Inventory(db.Model):
    __tablename__="inventory"
    id = db.Column('id',db.Integer, primary_key=True)
    products = db.relationship('Product', backref='inventories', lazy=True)
    stock = db.Column('stock', db.Integer)
    date_hour = db.Column('date_hour', db.String(30))

    def __init__(self, description, stock, date_hour):
        self.description = description
        self.stock = stock
        self.date_hour = date_hour