from app import db

class Inventory(db.Model):
    __tablename__="Inventory"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(30), db.ForeignKey('product.description'), nullable=False)
    stock = db.Column(db.Integer)
    date_hour = db.Column(db.String(30))

    def __init__(self, description, stock, date_hour):
        self.description = description
        self.stock = stock
        self.date_hour = date_hour