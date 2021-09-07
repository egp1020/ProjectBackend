from flask import jsonify, request
from flask import Blueprint
from controllers import category


category_blueprint = Blueprint('category_blueprint', __name__)
@category_blueprint.route('/categories', methods=["GET"])
def get():
    print("Aquí estoy")
    categories = category.get()
    return jsonify(categories)


@category_blueprint.route('/category', methods=["POST"])
def insert():
    category_datails = request.get_json()
    name = category_details["name"]
    photo = category_details["photo"]
    description = category_details["description"]
    result = category_datails.insert(name, photo, description)
    return jsonify(result)


@category_blueprint.route('/category', methods=["PUT"])
def update():
    category_datails = request.get_json()
    id = category_details["id"]
    photo = category_details["photo"]
    name = category_details["name"]
    description = category_details["description"]
    result = category.update(id, name, photo, description)
    return jsonify(result)


@category_blueprint.route('/category/<int:id>', methods=["DELETE"])
def delete(id):
    result = category.delete(id)
    return jsonify(result)


@category_blueprint.route('/category', methods=["GET"])
def getCategory(id):
    getCategory = category.get_by_id(id)
    return jsonify(getCategory)
