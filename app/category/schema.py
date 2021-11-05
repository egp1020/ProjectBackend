from app import ma
from .model import CategoryModel
from app.product.schema import ProductSchema


class CategorySchema(ma.SQLAlchemyAutoSchema):
    """Takes the Category model and defines a automatic schema to serialization"""

    class Meta:
        model = CategoryModel
        load_instance = True

    products = ma.Nested(ProductSchema, many=True)