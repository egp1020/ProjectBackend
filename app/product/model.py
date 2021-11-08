from app import db
""" from app.inventory.model import InventoryModel
from app.tax.model import TaxModel
from app.category.model import CategoryModel """


class ProductModel(db.Model):
    """Defines a Product model"""
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key = True)
    photo = db.Column(db.Text)
    description = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.Text)
    tax_id = db.Column(db.Integer, db.ForeignKey("tax.id"), nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    category_rs = db.relationship("CategoryModel", back_populates="product")
    inventory_rs = db.relationship("InventoryModel", back_populates="product")
    tax_rs = db.relationship("TaxModel", backref="product")

    def __init__(self, photo, description, category_id, quantity, price, tax_id, barcode):
        """Initialize a ProductModel instance"""
        self.photo = photo
        self.description = description
        self.category_id = category
        self.quantity = quantity
        self.price = price
        self.tax_id = tax
        self.barcode = barcode

    def __repr__(self):
        """Describes a ProductModel object"""
        return f'<Product {self.description}>'


