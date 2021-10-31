from flask import Flask
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app,
            version = "1.0",
            title = "Shop Managenment",
            description = "A simple ShopMVC API")


name_space = api.namespace('Category', description='Category endpoints')

category = api.model('Category', {
    'id':field.Integer(readonly=True, description='The category unique identifier'),
    'photo':field.Text(required=True, description=''),
    'name' : fields.String(required=True, description=''),
    'description' : fields.String(required=True, description=''),
})
@name_space.route('/')
class CategoryDoc(Resource):
    def get(self):
        return {
            {
                "id":"Number",
                "photo":"string",
                "name":"string",
                "description":"string"
            }
        }

    def getCategory(id):
        return {
            {
                "id":"1",
                "photo":"string",
                "name":"string",
                "description":"string"
            }
        }

    def createCategory():
        pass

    def updateCategory(id):
        pass

    def deleteCategory(id):
        pass


name_space = api.namespace('Inventory', description='Main APIs')

@name_space.route('/')
class InventoryDoc(Resource):
    def get():
        pass

    def getProductInventory(id):
        pass

    def createProductInventory():
        pass

    def updateProductInventory(id):
        pass

    def deleteProductInventory(id):
        pass

