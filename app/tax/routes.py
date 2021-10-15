from flask import jsonify, request
from flask import Blueprint
from app.tax.controller import TaxController

bptax = Blueprint('bptax', __name__, template_folder='templates')
controller = TaxController()

@bptax.route('/tax/', methods=["GET"])
def get():
    taxs = controller.getTaxAll()
    return jsonify(taxs)

@bptax.route('/tax/<id>', methods=["GET"])
def getTax(id):
    tax = controller.getTax(id)
    return jsonify(tax)

@bptax.route('/tax/', methods=["POST"])
def createTax():
    tax = {
        'taxType': request.json["taxType"],
        'rate': request.json["rate"]
    }
    taxs = controller.insertTax(tax)
    return taxs

@bptax.route('/tax/<id>/', methods=["PUT"])
def updateTax(id):
    tax = {
        'taxType': request.json["taxType"],
        'rate': request.json["rate"]
    }
    taxs = controller.updateTax(tax, id)
    return taxs

@bptax.route('/tax/<id>/', methods=["DELETE"])
def deleteTax(id):
    taxs = controller.deleteTax(id)
    return taxs