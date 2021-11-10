from app import ma
from .model import ProductModel


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        include_fk = True
        include_relationships = True
