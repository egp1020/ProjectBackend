from app import ma
from .model import ProductModel

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        load_only = ("Category",)
        include_fk = True