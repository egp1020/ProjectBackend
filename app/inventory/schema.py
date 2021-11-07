from app import ma
from .model import InventoryModel

class InventorySchema(ma.SQLAlchemyAutoSchema):
    """Takes the Inventory model and defines a automatic schema to serialization"""

    class Meta:
        model = InventoryModel
        include_fk = True
        load_instance = True

    products = ma.Nested(ProductSchema, many=True)