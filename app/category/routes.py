from .controller import CategoryController

from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource, fields

controller = CategoryController()
category_app = Blueprint('category_app', __name__, url_prefix='/app/')
category_api = Namespace('category_api', description='Category operations', path='/category/')

category_schema = category_ns.model('Category model', {
    'id':fields.Integer(readonly=True, description='The category unique identifier'),
    'photo':fields.String('Photo of the category'),
    'name':fields.String('Name of the category'),
    'description':fields.String('Description of the category')
})


@category_api.route('/')
class CategoryList(Resource):
    """Shows a list of all categories and lets you POST to add new tasks"""
    @category_api.doc('list_categories')
    @category_api.marshal_list_with(category_schema)
    def get(self):
        """List all categories"""
        categories = controller.get_category_all()
        return jsonify(categories)

    @category_api.doc('create_category')
    @category_api.expect(category_schema)
    @category_api.marshal_list_with(category_schema, code=201)
    def post(self):
        """Creates a new category"""
        category = {
            'name': request.json["name"],
            'photo': request.json["photo"],
            'description': request.json["description"]
        }
        new_category = controller.insert_category(category)
        return new_category, 201


@category_api.route("/<int:id>")
@category_api.response(202, "OK")
@category_api.response(404, "Category not found")
@category_api.response(404, "Mapping Key Error")
@category_api.param("id", "The category identifier")
class Category(Resource):
    @category_api.doc('get_category')
    @category_api.marshal_list_with(category_schema)
    def get(self, id):
        """Lists of all productos for a particular category """
        category = controller.get_category(id)
        return jsonify(category)

    @category_api.doc('update_category')
    @category_api.expect(category_schema)
    @category_api.marshal_list_with(category_schema)
    def update(self, id):
        """Update a category given its identifier"""
        category = {
            'photo': request.json["photo"],
            'name': request.json["name"],
            'description': request.json["description"]
        }
        category_update = controller.update_category(category, id)
        return category_update

    """Deletes a specific category"""
    @category_api.doc('dalete_category')
    @category_api.expect(category_schema)
    @category_api.response(204, "Category deleted")
    def delete(self, id):
        category = controller.delete_category(id)
        return category, 204
