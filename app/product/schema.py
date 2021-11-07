from app import ma
from .model import ProductModel
# from app.inventory.schema import InventorySchema

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        include_fk = True
        load_instance = True
        #load_only = ("Category",)

    # inventory = ma.Nested(InventorySchema)