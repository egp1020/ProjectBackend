import  base64
import os, flask
import sys
from sqlalchemy import or_
from app import app, db
from model import Product

class ProductController:
    def getProductAll(self):
        products = Product.query.all()
        product = []

        for element in products:
            product.append({
                'id':element.id,
                'photo':element.photo,
                'description':element.description,
                'category':element.category,
                'quantity':element.quantity,
                'stock':element.stock,
                'price':element.price,
                'tax':element.tax,
                'barcode':element.barcode
            })
        return product

    def getProduct(self, id):
        products = []
        product = Product.query.filter_by(id=id).first()

        if product is not None:
            products.append({
                'photo':product.photo,
                'description':product.description,
                'category':product.category,
                'quantity':product.quantity,
                'stock':product.stock,
                'price':product.price,
                'tax':product.tax,
                'barcode':product.barcode
            })
        else:
            products.append({
                'messages':'no se encontro id.',
            })
        return products

    def insertProduct(self, product):
        cccccccccccc
        product = Product.query.filter_by(id = id).first()
        if product is not None:
            data = Product(photo, description, category, quantity, stock, price, tax, barcode)
            db.session.add(data)
            db.session.commit()

            message = "El registro se hizo con éxito"
        else:
            message = "El registro no se logro."
        return message

# Agregar los otros campos
    def updateProduct(self, product):
        photo = product["photo"]
        description = product["description"]
        category = product["category"]
        quantity = product["quantity"]
        stock = product["stock"]
        price = product["price"]
        tax = product["tax"]
        barcode = product["barcode"]
        product = Product.query.filter_by(id=id).first()
        if product is not None:
            product.photo = photo
            product.description = description
            product.category = category
            product.quantity = quantity
            product.stock = stock
            product.price = price
            product.tax = tax
            product.barcode = barcode
            db.session.add(product)
            db.session.commit()
            message = "El producto se actualizo correctamente"
        else:
            message = "La actualización no se pudo realizar con éxito"
        return message


    def deleteProduct(self, id):
        product = Product.query.filter_by(id=id).first()
        if product is not None:
            db.session.delete(product)
            db.session.commit()
            message = "El producto ha sido eliminado con éxito."
        else:
            message = "El producto no se pudo eliminar."
        return message