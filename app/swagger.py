""" from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app,
            version = "1.0",
            title = "Shop Managenment",
            description = "Manage  buys")


name_space = api.namespace('Category', description='Main APIs')

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
 """
from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)

if __name__ == '__main__':
    app.run(debug=True)