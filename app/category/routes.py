from flask import jsonify, request
from category import category

@bpcategory.route('/categories', methods=["GET"])
def get():
    categories = category().get()
    return jsonify(categories)


@bpcategory.route('/category/<id>', methods=["GET"])
def getCategory(id):
    getCategory = category().get_by_id(id)
    return jsonify(getCategory)


@bpcategory.route('/category', methods=["POST"])
def insert():
    categoryDetail = request.get_json()
    name = categoryDetail["name"]
    photo = categoryDetail["photo"]
    description = categoryDetail["description"]
    result = category().insert(name, photo, description)
    return jsonify(result)


@bpcategory.route('/category', methods=["PUT"])
def update():
    categoryDetail = request.get_json()
    id = categoryDetail["id"]
    photo = categoryDetail["photo"]
    name = categoryDetail["name"]
    description = categoryDetail["description"]
    result = category().update(id, name, photo, description)
    return jsonify(result)


@bpcategory.route('/category', methods=["DELETE"])
def delete(id):
    result = category().delete(id)
    return jsonify(result)
