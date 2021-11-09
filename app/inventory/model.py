from app import db
from datetime import datetime

class InventoryModel(db.Model):
    """Defines a InventoryModel model"""
    __tablename__="inventory"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    stock = db.Column(db.Integer)
    date_created = db.Column( db.DateTime, nullable=False)

    product_relationship = db.relationship('ProductModel', backref='inventory', lazy=True, uselist=False)

    def __init__(self, product_id, stock):
        self.product_id = product_id
        self.stock = stock
        self.date_created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")