from app import ma
from app.product.schema import ProductSchema
from .model import CategoryModel


class CategorySchema(ma.SQLAlchemyAutoSchema):
    """Takes the Category model and defines a automatic schema to serialization"""

    class Meta:
        model = CategoryModel
        load_instance = True
        include_fk = True
        include_relationships = True

    products = ma.Nested(ProductSchema, many=True)