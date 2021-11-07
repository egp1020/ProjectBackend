from app import db

class CategoryModel(db.Model):
    """Defines a CategoryModel model"""
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(20), unique = True)
    description = db.Column(db.String(300))

    products = db.relationship('Product', backref='category', lazy=True)

    def __init__(self, photo, name, description):
        """Initialize a CategoryModel instance"""
        self.photo = photo
        self.name = name
        self.description = description

    def __repr__(self):
        """Describes a CategoryModel object"""
        return f'<Category {self.name}>'
