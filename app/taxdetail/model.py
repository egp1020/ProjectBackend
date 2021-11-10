from app import db

class TaxDetailModel(db.Model):
    """Defines a Tax Detail model"""
    __tablename__ = "taxDetail"
    id = db.Column(db.Integer, primary_key = True)
    tax_id = db.Column(db.Integer, db.ForeignKey("tax.id"))
    amount_buy = db.Column(db.Float, nullable=False)
    base_buy = db.Column(db.Float, nullable=False)
    value_tax = db.Column(db.Float)

    tax_relationship = db.relationship("TaxModel", backref="taxDetail")

    def __init__(self, tax_id, amount_buy, base_buy, value_tax):
        self.tax_id = tax_id
        self.amount_buy = amount_buy
        self.base_buy = base_buy
        self.value_tax = value_tax