from flask import jsonify, request
from flask import Blueprint
from src.inventory.inventory import inventory


bpinventory = Blueprint('bpinventory', __name__)

@bpinventory.route('/productsInventory', methods=["GET"])
def get():
    inventory = inventory().get()
    return jsonify(inventory)

@bpinventory.route('/productInventory', methods=["GET"])
def getProductInventory(id):
    getProductInventory = inventory().get_by_id()
    return jsonify(getProductInventory)

@bpinventory.route('/productInventory', methods=["POST"])
def insert():
    inventoryDetail = request.get_json()
    name = inventoryDetail["name"]
    photo = inventoryDetail["photo"]
    description = inventoryDetail["description"]
    result =  inventory().insert(name, photo, description)
    return jsonify(result)

@bpinventory.route('/inventory', methods=["POST"])
def update():
    inventoryDetail = request.get_json()
    id = inventoryDetail["id"]
    name = inventoryDetail ["name"]
    photo = inventoryDetail ["photo"]
    description = inventoryDetail ["description"]
    result =  inventory().update(id, name, photo, description)
    return jsonify(result)




