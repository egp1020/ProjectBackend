from app import db


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key = True)
    photo = db.Column(db.Text)
    description = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    quantity = db.Column(db.Float)
    inventory_id = db.Column(db.Float, db.ForeignKey("inventory.id"), nullable = False, unique=True)
    price = db.Column(db.Float, nullable=False)
    tax_id = db.Column(db.String(7), db.ForeignKey("tax.id"), nullable = False)
    barcode = db.Column(db.UnicodeText)

    def __init__(self, photo, description, category, quantity, inventory, price, tax, barcode):
        self.photo = photo
        self.description = description
        self.category_id = category
        self.quantity = quantity
        self.inventory_id = inventory
        self.price = price
        self.tax_id = tax
        self.barcode = barcode


