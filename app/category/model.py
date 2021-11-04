from app import db
from app.product.model import ProductModel

class CategoryModel(db.Model):
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(20), unique = True)
    description = db.Column(db.String(300))

    products = db.relationship('Product', backref='category', lazy=True)

    def __init__(self, photo, name, description):
        self.photo = photo
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Category {self.name}>'
