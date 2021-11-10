from app import ma
from app.product.schema import ProductSchema
from .model import InventoryModel


class InventorySchema(ma.SQLAlchemyAutoSchema):
    """Takes the Inventory model and defines a automatic schema to serialization"""

    class Meta:
        model = InventoryModel
        include_fk = True
        load_instance = True
        include_relationship = True