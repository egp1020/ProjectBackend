from app import db, ma
from app.product.model import Product

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(20), unique = True)
    description = db.Column(db.String(300))
    product = db.relationship('Product', backref='category', lazy=True)

    def __init__(self, photo, name, description):
        self.photo = photo
        self.name = name
        self.description = description

class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Category
        include_fk = True

    id = ma.auto_field()
    photo = ma.auto_field()
    name = ma.auto_field()
    description = ma.auto_field()
