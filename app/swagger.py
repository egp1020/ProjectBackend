from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, version="1.0", title="Product management ", description="Manage orders")


name_space = api.namespace('Category', description='Main APIs')

@name_space.route('/')
class CategoryDoc(Resource):
    def get(self):
        return {
            {
                "id":"1",
                "photo":"string",
                "name":"string",
                "description":"string"
            },
            {
                "id":"2",
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

if __name__ == '__main__':
    app.run(debug=True)