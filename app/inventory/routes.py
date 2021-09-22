from flask import jsonify, request
from inventory import bpinventory

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
    description = inventoryDetail["description"]
    stock = inventoryDetail["stock"]
    date_hour = inventoryDetail["date_hour"]
    result =  inventory().insert(description, stock, date_hour)
    return jsonify(result)

@bpinventory.route('/inventory', methods=["POST"])
def update():
    inventoryDetail = request.get_json()
    id = inventoryDetail["id"]
    description = inventoryDetail ["description"]
    stock = inventoryDetail ["stock"]
    date_hour = inventoryDetail ["date_hour"]
    result =  inventory().update(id, description, stock, date_hour)
    return jsonify(result)




