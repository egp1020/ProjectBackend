from flask import jsonify, request
from flask import Blueprint
from app.category.controller import CategoryController

bpcategory = Blueprint('bpcategory', __name__, template_folder='templates')
controller = CategoryController()

@bpcategory.route('/category/', methods=["GET"])
def get():
    categories = controller.getCategoryAll()
    return jsonify(categories)


@bpcategory.route('/category/<id>/', methods=["GET"])
def getCategory(id):
    category = controller.getCategory(id)
    return jsonify(category)


@bpcategory.route('/category/', methods=["POST"])
def createCategory():
    newCategory = {
        'name': request.json["name"],
        'photo': request.json["photo"],
        'description': request.json["description"]
    }
    categories = controller.insertCategory(newCategory)
    return categories


@bpcategory.route('/category/<id>/', methods=["PUT"])
def updateCategory(id):
    category = {
        'photo': request.json["photo"],
        'name': request.json["name"],
        'description': request.json["description"]
    }
    categories = controller.updateCategory(category)
    return categories


@bpcategory.route('/category/<id>/', methods=["DELETE"])
def deleteCategory(id):
    categories = controller.deleteCategory(id)
    return categories
