from flask import jsonify, request
from flask import Blueprint
from .category import category

bpcategory = Blueprint('bpcategory', __name__, template_folder='templates')
@bpcategory.route('/category/', methods=["GET"])
def get():
    categories = category().get()
    return jsonify(categories)


@bpcategory.route('/category/<id>/', methods=["GET"])
def getCategory(id):
    get_category = category().get_by_id(id)
    return jsonify(get_category)


@bpcategory.route('/category/', methods=["POST"])
def create():
    categoryDetail = request.get_json()
    id = categoryDetail["id"]
    name = categoryDetail["name"]
    photo = categoryDetail["photo"]
    description = categoryDetail["description"]
    result = category().create(name, photo, description)
    return jsonify(result)


@bpcategory.route('/category/<id>/', methods=["PUT"])
def update(id):
    categoryDetail = request.get_json()
    photo = categoryDetail["photo"]
    name = categoryDetail["name"]
    description = categoryDetail["description"]
    result = category().update(id, name, photo, description)
    return jsonify(result)


@bpcategory.route('/category/<id>/', methods=["DELETE"])
def delete(id):
    result = category().delete(id)
    return jsonify(result)
