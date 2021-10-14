from flask import jsonify, request
from flask import Blueprint
from app.inventory.controller import InventoryController

bpinventory = Blueprint('bpinventory', __name__, template_folder='templates')
controller = InventoryController()

@bpinventory.route('/productInventory/', methods=["GET"])
def get():
    products = controller.getProductInventoryAll()
    return jsonify(products)

@bpinventory.route('/productInventory/<id>/', methods=["GET"])
def getProductInventory(id):
    product = controller.getProductInventory(id)
    return jsonify(product)

@bpinventory.route('/productInventory/', methods=["POST"])
def createProductInventory():
    product = {
        'product': request.json["product"],
        'stock':request.json["stock"],
        'date_created':request.json["date_created"]
    }
    products = controller.insertProductInventory(product)
    return products

@bpinventory.route('/productInventory/<id>/', methods=["PUT"])
def updateProductInventory(id):
    product = {
        'product': request.json["product"],
        'stock':request.json["stock"],
        'date_created':request.json["date_created"]
    }
    products = controller.updateProductInventory(product, id)
    return products

@bpinventory.route('/productInventory/<id>/', methods=["DELETE"])
def deleteProductInventory(id):
    products = controller.deleteProductInventory(id)
    return products
