from flask import jsonify, request
from flask import Blueprint
from src.controllers.category import category


bpcategory = Blueprint('bpcategory', __name__)


@bpcategory.route('/categories', methods=["GET"])
def get():
    print("hola")
    categories = category().get()
    return jsonify(categories)


@bpcategory.route('/category', methods=["GET"])
def getCategory(id):
    getCategory = category.get_by_id(id)
    return jsonify(getCategory)


@bpcategory.route('/category', methods=["POST"])
def insert():
    category_details = request.get_json()
    name = category_details["name"]
    photo = category_details["photo"]
    description = category_details["description"]
    result = category_details.insert(name, photo, description)
    return jsonify(result)


@bpcategory.route('/category', methods=["PUT"])
def update():
    category_datails = request.get_json()
    id = category_details["id"]
    photo = category_details["photo"]
    name = category_details["name"]
    description = category_details["description"]
    result = category.update(id, name, photo, description)
    return jsonify(result)


@bpcategory.route('/category', methods=["DELETE"])
def delete(id):
    result = category.delete(id)
    return jsonify(result)
