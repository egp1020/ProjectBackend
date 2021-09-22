from flask import jsonify, request
from flask import Blueprint
from .product import product


bpproduct = Blueprint('bpproduct', __name__, template_folder='templates')

@bpproduct.route('/products/', methods=["GET"])
def get():
    product = product().get()
    return jsonify(product)

@bpproduct.route("/product/<id>/", methods=["GET"])
def getProduct(id):
    getProduct = product().get_by_id()