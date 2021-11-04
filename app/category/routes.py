from .controller import CategoryController
from .schema import CategorySchema

from flask import jsonify, request
from flask_restx import Namespace, Resource, fields

controller = CategoryController()

category_ns = Namespace('category', description='Main APIs')
categories_ns = Namespace('categories', description='scs')


category_schema = category_ns.model('Category model', {
    'id':fields.Integer(readonly=True, description='The category unique identifier'),
    'photo':fields.String('Photo of the category'),
    'name':fields.String('Name of the category'),
    'description':fields.String('Description of the category')
})

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

@api.route('/')
class CategoryList(Resource):
    """Shows a list of all categories and lets you POST to add new tasks"""
    @api.doc('list_categories')
    @api.marshal_list_with(category_schema)
    def get(self):
        """List all categories"""
        data_category = controller.getCategoryAll()
        print(data_category)
        return jsonify(categories_schema.dump(data_category))

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
        newCategory = controller.insertCategory(category)
        return newCategory, 201

@api.route("/<int:id>")
@api.response(202, "OK")
@api.response(404, "Category not found")
@api.response(404, "Mapping Key Error")
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
