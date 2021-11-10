from app import db

class TaxModel(db.Model):
    __tablename__="tax"
    id = db.Column(db.Integer, primary_key=True)
    tax_type = db.Column(db.String(7), unique=True, nullable = False)
    rate = db.Column(db.Float, nullable = False)

    def __init__(self, tax_type, rate):
        self.tax_type = tax_type
        self.rate = rate