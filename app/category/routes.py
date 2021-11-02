from flask import jsonify, request
from flask import Blueprint
from app.category.controller import CategoryController
from flask_restx import Namespace, Resource, fields

controller = CategoryController()
bpcategory = Blueprint('bpcategory', __name__, url_prefix='/categories/')
api = Namespace('categories', description='Main APIs')

category_schema = api.model('Category model', {
    'id':fields.Integer(readonly=True, description='The category unique identifier'),
    'photo':fields.String(),
    'name':fields.String(),
    'description':fields.String()
})

@api.route('/')
@bpcategory.route('/')
class CategoryList(Resource):
    """Shows a list of all categories and lets you POST to add new tasks"""
    @api.doc('list_categories')
    @api.marshal_list_with(category_schema)
    def get(self):
        """List all categories"""
        data_category = controller.getCategoryAll()
        print(data_category)
        return jsonify(data_category)

    @api.doc('create_category')
    @api.expect(category_schema)
    @api.marshal_list_with(category_schema, code=201)
    def post(self):
        """Creates a new category"""
        category = {
            'name': request.json["name"],
            'photo': request.json["photo"],
            'description': request.json["description"]
        }
        data_category = controller.insertCategory(category)
        return data_category, 201

@api.route("/<int:id>")
@bpcategory.route('/<int:id>')
@api.response(404, "Category not found")
@api.param("id", "The category identifier")
class CategoryL(Resource):
    @api.doc('get_category')
    @api.marshal_list_with(category_schema)
    def getCategory(self, id):
        """Lists of all productos for a particular category """
        data_category = controller.getCategory(id)
        return jsonify(data_category)

    @api.doc('update_category')
    @api.expect(category_schema)
    @api.marshal_list_with(category_schema)
    def updateCategory(self, id):
        """Update a category given its identifier"""
        category = {
            'photo': request.json["photo"],
            'name': request.json["name"],
            'description': request.json["description"]
        }
        data_category = controller.updateCategory(category, id)
        return data_category

    """Deletes a specific category"""
    @api.doc('dalete_category')
    @api.expect(category_schema)
    @api.response(204, "Category deleted")
    def deleteCategory(self, id):
        data_category = controller.deleteCategory(id)
        return data_category, 204
