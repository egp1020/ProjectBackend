from flask import jsonify, request
from app.category.controller import CategoryController
from flask_restx import Namespace, Resource, fields

controller = CategoryController()
api = Namespace('categories', description='Main APIs')

category = api.model('Category model', {
    'id':fields.Integer(readonly=True, description='The category unique identifier'),
    'photo':fields.String(),
    'name':fields.String(),
    'description':fields.String()
})

@api.route('/')
class CategoryList(Resource):
    @api.doc('list_categories')
    @api.marshal_list_with(category)
    def get():
        """List all categories"""
        categories = controller.getCategoryAll()
        return jsonify(categories)

    @api.doc('create_category')
    @ns.expect(todo)
    @api.marshal_list(category, code=201)
    def post():
        "Creates a new category"
        category = {
            'name': request.json["name"],
            'photo': request.json["photo"],
            'description': request.json["description"]
        }
        categories = controller.insertCategory(category)
        return categories, 201

    #@api.route('/category/<id>/', methods=["GET"])
    def getCategory(id):
        category = controller.getCategory(id)
        return jsonify(category)

    #@api.route('/category/<id>/', methods=["PUT"])
    def updateCategory(id):
        category = {
            'photo': request.json["photo"],
            'name': request.json["name"],
            'description': request.json["description"]
        }
        categories = controller.updateCategory(category, id)
        return categories


    #@api.route('/category/<id>/', methods=["DELETE"])
    def deleteCategory(id):
        categories = controller.deleteCategory(id)
        return categories
