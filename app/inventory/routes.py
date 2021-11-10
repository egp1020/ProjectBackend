from .controller import InventoryController

from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource, fields

controller = InventoryController()
inventory_app = Blueprint('inventory_app', __name__, url_prefix='/app/')
inventory_api = Namespace('inventory_api', description='Inventory operations', path='/inventory/')

inventory_schema = inventory_api.model('Inventory model', {
    'id':fields.Integer(readonly=True, description='The product in inventory unique identifier'),
    'product_id':fields.Integer('The product unique identifier '),
    'stock':fields.Integer('Stock of the product in inventory'),
    'date_created':fields.DateTime('Product added date'),
})


@inventory_api.route('/')
class InventoryList(Resource):
    """Shows a list of all products in inventory and lets you POST to add new products"""
    @inventory_api.doc('List_products_in_inventory')
    @inventory_api.marshal_list_with(inventory_schema)
    def get(self):
        """List all products in inventory"""
        products = controller.get_inventory_all()
        return jsonify(products)

    @inventory_api.doc('Add_product')
    @inventory_api.expect(inventory_schema)
    @inventory_api.marshal_list_with(inventory_schema)
    def post(self):
        """Add a new product"""
        product = {
            'product': request.json["product"],
            'stock':request.json["stock"],
        }
        products = controller.insert_inventory(product)
        return products, 201

@inventory_api.route("/<int:id>")
@inventory_api.response(202, "OK")
@inventory_api.response(404, "Product not found")
@inventory_api.response(404, "Mapping Key Error")
@inventory_api.param("id", "The inventory identifier")
class Inventory(Resource):
    @inventory_api.doc('get_product_inventory')
    @inventory_api.marshal_list_with(inventory_schema)
    def get(self, id):
        """Lists product in inventory"""
        product = controller.get_inventory(id)
        return jsonify(product)

    @inventory_api.doc('update_product_inventory')
    @inventory_api.expect(inventory_schema)
    @inventory_api.marshal_list_with(inventory_schema)
    def put(self, id):
        """Update a product in inventory given its identifier"""
        product = {
            'product': request.json["product"],
            'stock':request.json["stock"],
        }
        product_update = controller.update_inventory(product, id)
        return product_update

    @inventory_api.doc('dalete_product_inventory')
    @inventory_api.expect(inventory_schema)
    @inventory_api.response(204, "Product deleted")
    def delete(self, id):
        """Deletes a specific product in inventory"""
        product = controller.delete_inventory(id)
        return product, 204
