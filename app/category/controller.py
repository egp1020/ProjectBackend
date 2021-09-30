
import base64
import os, flask
import sys
from sqlalchemy import or_
from app import app, db
from model import Category

class CategoryController:
    def getCategoryAll(self):
        categories = Category.query.all()
        category = []

        for element in categories:
            category.append({
                'id':element.id,
                'photo':element.photo,
                'name':element.name,
                'description':element.description
            })
        return category

    def getCategory(self, id):
        categories = []
        category = Category.query.filter_by(id=id).first()

        if category is not None:
            categories.append({
                'id':category.id,
                'photo':category.photo,
                'name':category.name,
                'description':category.description
            })
        else:
            categories.append({
                'messages':'no se encontro id.',
            })
        return categories

    def insertCategory(self, category):
        photo = category["photo"]
        name = category["name"]
        description = category["description"]
        category = Category.query.filter_by(id = id).first()
        if category is not None:
            data = Category(photo, name, description)
            db.session.add(data)
            db.session.commit()

            message = "El registro se hizo con éxito"
        else:
            message = "El registro no se logro."
        return message

    def updateCategory(self, category):
        photo = category["photo"]
        name = category["name"]
        description = category["description"]
        category = Category.query.filter_by(id=id).first()
        if category is not None:
            category.photo = photo
            category.name = name
            category.description = description
            db.session.add(category)
            db.session.commit()
            message = "La categoría se actualizo correctamente"
        else:
            message = "La actualización no se pudo realizar con éxito"
        return message


    def deleteCategory(self, id):
        category = Category.query.filter_by(id=id).first()
        if category is not None:
            db.session.delete(category)
            db.session.commit()
            message = "La categoría ha sido eliminada con éxito."
        else:
            message = "La categoría no se pudo eliminar."
        
        return message

