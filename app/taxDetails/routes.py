from flask import jsonify, request
from flask import Blueprint
from app.taxDetails.controller import TaxDetailsController

bptaxdetails = Blueprint('bptaxdetails', __name__, template_folder='templates')
controller = TaxDetailsController()

@bptaxdetails.route('/taxDetail/', methods=["GET"])
def get():
    taxsDetails = controller.getTaxDetailsAll()
    return jsonify(taxsDetails)

@bptaxdetails.route('/taxDetail/<id>/', methods=["GET"])
def getTaxDetail(id):
    taxDetails = controller.getTaxDetails(id)
    return jsonify(taxDetails)

@bptaxdetails.route('/taxDetail/', methods=["POST"])
def createTaxDetail():
    taxDetails = {
        'taxType': request.json["taxType"],
        'amountBuy': request.json["amountBuy"],
        'baseBuy': request.json["baseBuy"],
        'valueTax': request.json["valueTax"]
    }

    taxsDetails = controller.insertTaxDetails(taxDetails)
    return taxsDetails

@bptaxdetails.route('/taxDetail/<id>/', methods=["UPDATE"])
def updateTaxDetail(id):
    taxDetails = {
        'taxType': request.json["taxType"],
        'amountBuy': request.json["amountBuy"],
        'baseBuy': request.json["baseBuy"],
        'valueTax': request.json["valueTax"]
    }

    taxsDetails = controller.updateTax(taxDetails)
    return taxsDetails

@bptaxdetails.route('/taxDetail/<id>/', methods=["DELETE"])
def deleteTaxDetail(id):
    taxsDetails = controller.deleteTax(id)
    return taxsDetails