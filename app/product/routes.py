from flask import jsonify, request
from flask import Blueprint
from .product import product


bpproduct = Blueprint('bpproduct', __name__, template_folder='templates')


@bpproduct.route('/product/', methods=["GET"])
def get():
    products = product().get()
    return jsonify(products)


@bpproduct.route("/product/<id>/", methods=["GET"])
def getProduct(id):
    get_product = product().get_by_id(id)
    return jsonify(get_product)


@bpproduct.route("/product/", methods=["POST"])
def create():
    productDetail = request.get_json()
    photo = productDetail["photo"]
    description = productDetail["description"]
    category = productDetail["category"]
    quantity = productDetail["quantity"]
    stock = productDetail["stock"]
    price = productDetail["price"]
    barcode = productDetail["barcode"]
    tax = productDetail["tax"]
    result = product().create(photo, description, category, quantity, stock, price, barcode, tax)
    return jsonify(result)


@bpproduct.route('/product/<id>/', methods=["PUT"])
def update(id):
    productDetail = request.get_json()
    photo = productDetail["photo"]
    description = productDetail["description"]
    category = productDetail["category"]
    quantity = productDetail["quantity"]
    stock = productDetail["stock"]
    price = productDetail["price"]
    barcode = productDetail["barcode"]
    tax = productDetail["tax"]
    result = product().update(id, photo, description, category, quantity, stock, price, barcode, tax)
    return jsonify(result)


@bpproduct.route('/product/<id>/', methods=["PUT"])
def delete(id):
    result = product().delete(id)
    return jsonify(result)
