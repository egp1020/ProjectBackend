from app import db
from .model import InventoryModel
from .schema import InventorySchema

inventory_schema = InventorySchema()
inventory_all_schema = InventorySchema(many=True)

PRODUCT_NOT_FOUND = "Product not found in inventory."
PRODUCT_ALREADY_EXISTS = "Product '{}' already exists in inventory."

class InventoryController:
    def get_inventory_all(self):
        products = InventoryModel.query.all()
        result = inventory_all_schema.dump(products)
        return result, 200

    def get_inventory(self, id):
        product = InventoryModel.query.filter_by(id=id).first()
        if product:
            return inventory_schema.dump(product)
        return {'message': PRODUCT_NOT_FOUND}, 404

    def insert_inventory(self, product):
        product_id = product["product_id"]
        inventory_find = InventoryModel.query.filter_by(product_id=product_id)
        if inventory_find:
            return {'message': PRODUCT_ALREADY_EXISTS}

        stock = product["stock"]
        new_product = InventoryModel(product_id, stock)
        db.session.add(new_product)
        db.session.commit()
        return inventory_schema.jsonify(new_product)

    def update_inventory(self, product, id):
        product_id = product["product_id"]
        stock = product["stock"]
        inventory_id = InventoryModel.query.get(id)
        if inventory_id:
            inventory_id.product = product
            inventory_id.stock = stock
            db.session.commit()
            return inventory_schema.jsonify(inventory_id)
        return {'message': PRODUCT_NOT_FOUND}, 404

    def delete_inventory(self, id):
        product = InventoryModel.query.filter_by(id = id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return inventory_schema.jsonify(product)
        return {'message': PRODUCT_NOT_FOUND}, 404

