from flask import jsonify, request
from flask import Blueprint
from .inventory import inventory

bpinventory = Blueprint('bpinventory', __name__, template_folder='templates')
@bpinventory.route('/productInventory/', methods=["GET"])
def get():
    inventory = inventory().get()
    return jsonify(inventory)

@bpinventory.route('/productInventory/<id>/', methods=["GET"])
def getProductInventory(id):
    get_productInventory = inventory().get_by_id(id)
    return jsonify(get_productInventory)

@bpinventory.route('/productInventory/', methods=["POST"])
def create():
    inventoryDetail = request.get_json()
    description = inventoryDetail["description"]
    stock = inventoryDetail["stock"]
    date_hour = inventoryDetail["date_hour"]
    result =  inventory().create(description, stock, date_hour)
    return jsonify(result)

@bpinventory.route('/productInventory/<id>/', methods=["POST"])
def update(id):
    inventoryDetail = request.get_json()
    description = inventoryDetail ["description"]
    stock = inventoryDetail ["stock"]
    date_hour = inventoryDetail ["date_hour"]
    result =  inventory().update(id, description, stock, date_hour)
    return jsonify(result)

@bpinventory.route('/productInventory/<id>/', methods=["DELETE"])
def delete(id):
    result = inventory().delete(id)
    return jsonify(result)


