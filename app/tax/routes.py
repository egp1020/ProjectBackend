from flask import jsonify, request
from flask import Blueprint
from .tax import tax

bptax = Blueprint('bptax', __name__, template_folder='templates')
@bptax.route('/tax/', methods=["GET"])
def get():
    taxs = tax().get()
    return jsonify(get_tax)

@bptax.route('/tax/<id>', methods=["GET"])
def getTax(id):
    get_tax = tax().get_by_id(id)
    return jsonify(get_tax)

@bptax.route('/tax/', methods=["POST"])
def create():
    taxDetail = request.get_json()
    taxType = taxDetail["taxType"]
    rate = taxDetail["rate"]
    result = tax().create(taxType, rate)
    return jsonify(result)

@bptax.route('/tax/<id>/', methods=[""])
def update(id):
    taxDetail = request.get_json()
    taxType = taxDetail["taxType"]
    rate = taxDetail["rate"]
    result = tax().update(id, taxType, rate)
    return jsonify(result)

@bptax.route('/tax/<id>/', methods=["DELETE"])
def delete(id):
    result = tax().delete(id)
    return jsonify(result)