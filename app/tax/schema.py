from marshmallow_sqlalchemy import load_instance_mixin
from app import ma
from app.product.schema import ProductSchema
from .model import TaxModel

class TaxSchema(ma.SQLAlchemyAutoSchema):
    model = TaxModel
    load_instance = True
    include_relationships = True

    products_relationship = ma.Nested(ProductSchema, many=True)