from .controller import ProductController

from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource, fields

controller = ProductController()
product_app = Blueprint('product_app', __name__, url_prefix='/app/')
product_api = Namespace('product_api', description='Product operations', path='/product/')

product_schema = product_api.model('Product', {
    'id': fields.Integer(readonly=True, description='The product unique identifier'),
    'photo': fields.String('Photo of the product'),
    'description': fields.String('Description of the product'),
    'category_id': fields.Integer('Category where are the product'),
    'quantity': fields.String('The number of products to buy'),
    'price': fields.String('Price of the product'),
    'tax_id': fields.Integer('Tax of the product'),
    'barcode': fields.String('Barcode identifier'),
})

@product_api.route("/")
class ProductList(Resource):
    """Shows a list of all products and lets you POST to add new"""
    @product_api.doc('list_products')
    @product_api.marshal_list_with(product_schema)
    def get():
        products = controller.get_product_all()
        return jsonify(products)

    @product_api.doc('create_product')
    @product_api.expect(product_schema)
    @product_api.marshal_list_with(product_schema, code=201)
    def post(self):
        """Creates a new product"""
        product = {
            'photo':request.files["photo"],
            'description': request.json["description"],
            'category': request.json["category"],
            'quantity': request.json["quantity"],
            'price': request.json["price"],
            'tax': request.json["tax"],
            'barcode': request.json["barcode"]
        }

        new_product = controller.insert_product(product)
        return new_product, 201

@product_api.route("/<int:id>")
@product_api.response(202, "OK")
@product_api.response(404, "Product not found")
@product_api.response(404, "Mapping Key Error")
@product_api.param("id", "The product identifier")
class Product(Resource):
    @product_api.doc('get_product')
    @product_api.marshal_list_with(product_schema)
    def get(self, id):
        """Lists a product by id"""
        product = controller.get_product(id)
        return jsonify(product)

    def update(self, id):
        """Update a category given its identifier"""
        product = {
            'photo':request.files["photo"],
            'description': request.json["description"],
            'category': request.json["category"],
            'quantity': request.json["quantity"],
            'price': request.json["price"],
            'tax': request.json["tax"],
            'barcode': request.json["barcode"]
        }

        product_update = controller.update_product(product, id)
        return product_update

    @product_api.doc('dalete_product')
    @product_api.expect(product_schema)
    @product_api.response(204, "Product deleted")
    def delete(id):
        product = controller.delete_category(id)
        return product, 204

@product_api.route("/<category_id>")
@product_api.response(202, "OK")
@product_api.response(404, "Products of the category not found")
@product_api.response(404, "Mapping Key Error")
@product_api.param("category_id", "The category identifier")
class ProductCategory(Resource):
    def get(category_id):
        products = controller.get_product_category(category_id)
        return jsonify(products)