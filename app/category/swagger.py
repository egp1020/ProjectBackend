from flask import Flask
from flask_restplus import Resource, fields
from app import api

name_space = api.namespace('Category', description='Main APIs')

category = api.model('Category model', {
    'id':fields.Integer(readonly=True, description='The category unique identifier'),
    'photo':fields.String(),
    'name':fields.String(),
    'description':fields.String()
})

@name_space.route('/')
class CategoryDoc(Resource):
    def get(self):
        return {
            "status":"Got new data"
        }

    def getCategory(id):
        return none

    def createCategory():
        return {
            "status":"Posted new data"
        }

    def updateCategory(id):
        pass

    def deleteCategory(id):
        pass
