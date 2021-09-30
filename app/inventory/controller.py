import  base64
import os, flask
import sys
from sqlalchemy import or_
from app import app, db
from app.inventory.model import Inventory

class InventoryController:
    def getProductInventoryAll(self):
        products = Inventory.query.all()
        inventory = []

        for product in products:
            inventory.append({
                'id':product.id,
                'description':product.description,
                'stock':product.stock,
                'date_hour':product.date_hour
            })
        return inventory

    def getProductInventory(self, id):
        products = []
        inventory = Inventory.query.filter_by(id=id).first()

        if inventory is not None:
            products.append({
                'id':inventory.id,
                'photo':inventory.photo,
                'name':inventory.name,
                'description':inventory.description
            })
        else:
            products.append({
                'message':'no se encontro id.',
            })
        return products

    def insertProductInventory(self, product):
        description = product["description"]
        stock = product["stock"]
        date_hour = product["date_hour"]
        product = Inventory.query.filter_by(id = id).first()
        if product is not None:
            data = Inventory(description, stock, date_hour)
            db.session.add(data)
            db.session.commit()

            message = "El registro del producto se realizo con éxito."
        else:
            message = "El registro del producto no fue éxitoso."
        return message

    def updateProductInventory(self, product):
        description = product["description"]
        stock = product["stock"]
        date_hour = product["date_hour"]
        product = Inventory.query.filter_by(id = id).first()
        if product is not None:
            product.description = description
            product.stock = stock
            product.date_hour = date_hour
            db.session.add(product)
            db.session.commit()
            message = "La actualización del producto se realizo con éxito."
        else:
            message = "El actualización del producto no fue éxitosa."
        return message

    def deleteProductInventory(self, id):
        product = Inventory.query.filter_by(id = id).first()
        if product is not None:
            db.session.delete(product)
            db.session.commit()
            message = "El producto ha sido eliminado con éxito."
        else:
            message = "El producto no se ha podido eliminar."
        return message

