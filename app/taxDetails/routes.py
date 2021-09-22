from flask import jsonify, request
from flask import Blueprint
from .taxDetails import taxDetails

bptaxDetails = Blueprint('bptaxDetails', __name__, template_folder='templates')
@bptaxDetails.route('/tax-detail/', methods=["GET"])
def get():
    tax_detail = taxDetails().get()
    return jsonify(tax_detail)

@bptaxDetails.route('/tax-detail/<id>/', methods=["GET"])
def get(id):
    get_taxDetails = taxDetails().get_by_id(id)
    return get_taxDetails

@bptaxDetails.route('/tax-detail/', methods=["POST"])
def create():
    taxDD = request.get_json()
    taxType = taxDD["taxType"]
    amountBuy = taxDD["amountBuy"]
    baseBuy = taxDD["baseBuy"]
    valueTax = taxDD["valueTax"]
    result = taxDetails().create(taxType, amountBuy, baseBuy, valueTax)
    return jsonify(result)

@bptaxDetails.route('/tax-detail/<id>/', methods=["UPDATE"])
def update(id):
    taxDD = request.get_json()
    taxType = taxDD["taxType"]
    amountBuy = taxDD["amountBuy"]
    baseBuy = taxDD["baseBuy"]
    valueTax = taxDD["valueTax"]
    result = taxDetails().update(id, taxType, amountBuy, baseBuy, valueTax)
    return jsonify(result)

@bptaxDetails.route('/tax-detail/<id>/', methods=["DELETE"])
def delete(id):
    result = taxDetails().delete(id)
    return jsonify(result)