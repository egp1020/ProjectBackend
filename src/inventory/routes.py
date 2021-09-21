from flask import jsonify, request
from flask import Blueprint
from controllers import inventory


bpinventory = Blueprint('bpinventory', __name__)

@bpinventory.route('/productsInventory', methods=["GET"])
def get():
    print("Aquí estoy")
    inventory = inventory.get()
    return "jsonify(inventory)"

@bpinventory.route('/productInventory', methods=["POST"])
def insert():
    inventory_datails = request.get_json()
    name = inventory_datails ["name"]
    photo = inventory_datails ["photo"]
    description = inventory_datails ["description"]
    result =  inventory_datails.insert(name, photo, description)
    return jsonify(result)
    
@bpinventory.route('/inventory', methods=["POST"])
def insert():
    inventory_datails = request.get_json()
    name = inventory_datails ["name"]
    photo = inventory_datails ["photo"]
    description = inventory_datails ["description"]
    result =  inventory_datails.insert(name, photo, description)
    return jsonify(result)   




