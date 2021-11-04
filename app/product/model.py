from app import db
from app.inventory.model import Inventory
from app.tax.model import Tax
from app.category.model import CategoryModel


class ProductModel(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key = True)
    photo = db.Column(db.Text)
    description = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey("Category.id"))
    price = db.Column(db.Float, nullable=False)
    tax_id = db.Column(db.Integer, db.ForeignKey("Tax.id"), nullable = False)
    barcode = db.Column(db.Text)

    category = db.relationship("Category", back_populates="products")
    inventory = db.relationship("Inventory", back_populates="products")
    tax = db.relationship("Tax", backref="products")

    def __init__(self, photo, description, category, quantity, inventory, price, tax, barcode):
        self.photo = photo
        self.description = description
        self.category_id = category
        self.quantity = quantity
        self.inventory_id = inventory
        self.price = price
        self.tax_id = tax
        self.barcode = barcode


