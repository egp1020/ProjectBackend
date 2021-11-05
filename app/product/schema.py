from app import ma
from .model import ProductModel
from app.inventory.schema import InventorySchema

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True
        #load_only = ("Category",)
        include_fk = True

    inventory = ma.Nested(InventorySchema)