from app import db
from app.taxdetail.model import TaxDetailModel

class TaxModel(db.Model):
    __tablename__="tax"
    id = db.Column(db.Integer, primary_key=True)
    tax_type = db.Column(db.String(7), unique=True, nullable = False)
    rate = db.Column(db.Float, nullable = False)

    products_relationship = db.relationship("ProductModel", backref='tax')
    tax_detail_relationship = db.relationship("TaxDetailModel", backref='tax')

    def __init__(self, tax_type, rate):
        self.tax_type = tax_type
        self.rate = rate