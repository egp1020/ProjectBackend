from app import db


class Tax(db.Model):
    __tablename__="tax"
    id = db.Column(db.Integer, primary_key=True)
    taxType = db.Column(db.String(7), unique=True, nullable = False)
    rate = db.Column(db.Float, nullable = False)
    products = db.relationship("Product", backref='taxs')

    def __init__(self, taxType, rate):
        self.taxType = taxType
        self.rate = rate