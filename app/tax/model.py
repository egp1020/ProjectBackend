from app import db


class Tax(db.Model):
    __tablename__="Tax"
    id = db.Column(db.Integer, primary_key=True)
    taxType = db.Column(db.String(7), unique=True, nullable = False)
    rate = db.Column(db.Float, nullable = False)

    def __init__(self, taxType, rate):
        self.taxType = taxType
        self.rate = rate