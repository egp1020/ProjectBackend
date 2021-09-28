from app import db

class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key = True)
    photo = db.Column(db.Text)
    description = db.Column(db.String(30))
    category = db.Column(db.String(20))
    quantity = db.Column(db.Float)
    stock = db.Column(db.Float, db.ForeignKey("inventory.stock"))
    price = db.Column(db.Float, nullable=False)
    tax = db.Column(db.String(7), nullable = False)
    barcode = db.Column(db.UnicodeText)

    def __init__(self, photo, description, category, quantity, stock, price, tax, barcode):
        self.photo = photo
        self.description = description
        self.category = category
        self.quantity = quantity
        self.stock = stock
        self.price = price
        self.tax = tax
        self.barcode = barcode


