from app import db
""" from app.product.model import ProductModel
from app.taxDetails.model import TaxDetailModel """


class TaxModel(db.Model):
    __tablename__="Tax"
    id = db.Column(db.Integer, primary_key=True)
    tax_type = db.Column(db.String(7), unique=True, nullable = False)
    rate = db.Column(db.Float, nullable = False)

    products = db.relationship("Product", backref='tax', uselist=False)
    products = db.relationship("TaxDetailModel", backref='tax')

    def __init__(self, tax_type, rate):
        self.tax_type = tax_type
        self.rate = rate