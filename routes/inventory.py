from flask import jsonify, request
from flask import Blueprint
from controllers import inventory



inventory_blueprint = Blueprint('inventory_blueprint', __name__)
@inventory_blueprint.route('/productsInventory', methods=["GET"])
def get():
    print("Aquí estoy")
    inventory = inventory.get()
    return jsonify(inventory)

@inventory_blueprint.route('/productInventory', methods=["POST"])
def insert():
    inventory_datails = request.get_json()
    name = inventory_datails ["name"]
    photo = inventory_datails ["photo"]
    description = inventory_datails ["description"]
    result =  inventory_datails.insert(name, photo, description)
    return jsonify(result)
    
@inventory_blueprint.route(rule)
def insert():
    inventory_datails = request.get_json()
    name = inventory_datails ["name"]
    photo = inventory_datails ["photo"]
    description = inventory_datails ["description"]
    result =  inventory_datails.insert(name, photo, description)
    return jsonify(result)   




