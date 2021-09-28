from app import db


class TaxDetails(db.Model):
    __tablename__ = "TaxDetails"
    id = db.Column(db.Integer, primary_key = True)
    taxType = db.Column(db.String(7), db.ForeignKey("tax.taxType"), nullable=False)
    amountBuy = db.Column(db.Float)
    baseBuy = db.Column(db.Float)
    valueTax = db.Column(db.Float)

    def __init__(self, taxType, amountBuy, baseBuy, valueTax):
        self.taxType = taxType
        self.amountBuy = amountBuy
        self.baseBuy = baseBuy
        self.valueTax = valueTax