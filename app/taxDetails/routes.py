from flask import jsonify, request
from flask import Blueprint
from .taxDetails import taxDetails

bptaxdetails = Blueprint('bptaxdetails', __name__, template_folder='templates')
@bptaxdetails.route('/taxDetail/', methods=["GET"])
def get():
    tax_detail = taxDetails().get()
    return jsonify(tax_detail)

@bptaxdetails.route('/taxDetail/<id>/', methods=["GET"])
def getTaxDetail(id):
    get_taxDetails = taxDetails().get_by_id(id)
    return get_taxDetails

@bptaxdetails.route('/taxDetail/', methods=["POST"])
def create():
    taxDD = request.get_json()
    taxType = taxDD["taxType"]
    amountBuy = taxDD["amountBuy"]
    baseBuy = taxDD["baseBuy"]
    valueTax = taxDD["valueTax"]
    result = taxDetails().create(taxType, amountBuy, baseBuy, valueTax)
    return jsonify(result)

@bptaxdetails.route('/taxDetail/<id>/', methods=["UPDATE"])
def update(id):
    taxDD = request.get_json()
    taxType = taxDD["taxType"]
    amountBuy = taxDD["amountBuy"]
    baseBuy = taxDD["baseBuy"]
    valueTax = taxDD["valueTax"]
    result = taxDetails().update(id, taxType, amountBuy, baseBuy, valueTax)
    return jsonify(result)

@bptaxdetails.route('/taxDetail/<id>/', methods=["DELETE"])
def delete(id):
    result = taxDetails().delete(id)
    return jsonify(result)