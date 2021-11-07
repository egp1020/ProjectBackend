from app import ma
from app.inventory.schema import InventorySchema
from .model import ProductModel


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        include_fk = True
        load_instance = True

    inventory = ma.Nested(InventorySchema)