from app import db
from app.tax.model import TaxModel


class TaxDetailModel(db.Model):
    """Defines a Tax model"""
    __tablename__ = "TaxDetail"
    id = db.Column(db.Integer, primary_key = True)
    tax_id = db.Column(db.Integer, db.ForeignKey("Tax.id"))
    amount_buy = db.Column(db.Float)
    base_buy = db.Column(db.Float)
    value_tax = db.Column(db.Float)

    tax = db.relationship("Tax", backref="taxsDetail")

    def __init__(self, tax_id, amount_buy, base_buy, value_tax):
        self.tax_id = tax_id
        self.amount_buy = amount_buy
        self.base_buy = base_buy
        self.value_tax = value_tax