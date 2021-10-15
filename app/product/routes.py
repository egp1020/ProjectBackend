import os
from datetime import date
from werkzeug.utils import secure_filename
from flask import jsonify, request
from flask import Blueprint
from app.product.controller import ProductController

bpproduct = Blueprint('bpproduct', __name__, template_folder='templates')
controller = ProductController()

@bpproduct.route("/product/", methods=["POST"])
def createProduct():
    product = {
        'photo':request.files["photo"],
        'description': request.json["description"],
        'category': request.json["category"],
        'quantity': request.json["quantity"],
        'stock': request.json["stock"],
        'price': request.json["price"],
        'tax': request.json["tax"],
        'barcode': request.json["barcode"]
    }

    products = controller.insertProduct(product)
    return products


@bpproduct.route('/product/<id>/', methods=["PUT"])
def updateProduct(id):
    product = {
        'photo':request.files["photo"],
        'description': request.json["description"],
        'category': request.json["category"],
        'quantity': request.json["quantity"],
        'stock': request.json["inventory"],
        'price': request.json["price"],
        'tax': request.json["tax"],
        'barcode': request.json["barcode"]
    }

    products = controller.updateProduct(product, id)
    return products


@bpproduct.route('/product/<id>/', methods=["PUT"])
def deleteProduct(id):
    products = controller.deleteProduct(id)
    return products

@bpproduct.route('/product/', methods=["GET"])
def get():
    products = controller.getProductAll()
    return jsonify(products)


@bpproduct.route("/product/<id>/", methods=["GET"])
def getProduct(id):
    product = controller.getProduct(id)
    return jsonify(product)

@bpproduct.route("/productCategory/<id>/", methods=["GET"])
def getProductCategory(id):
    product = controller.getProductCategory(id)
    return jsonify(product)