
import  base64
import os, flask
import sys
from sqlalchemy import or_
from app import app, db
from model import Category

class CategoryController:
    def getCategoryAll(self):
        categories = category.query.all()
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

            text = "El registro se hizo con éxito"
        else:
            text = "El registro no se logro."
        return text

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
            text = "La categoría se actualizo correctamente"
        else:
            text = "La actualización no se pudo realizar con éxito"
        return text


    def deleteCategory(self, id):
        category = Category.query.filter_by(id=id).first()
        if category is not None:
            db.session.delete(category)
            db.session.commit()
            text = "La categoría ha sido eliminada con éxito."
        else:
            text = "La categoría no se pudo eliminar."

