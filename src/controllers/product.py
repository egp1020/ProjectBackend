from flask import request, render_template, redirect, flash
from flask.views import MethodView
from src.db import cursor

class products(MethodView):
    def get():
        query = "SELECT * FROM products"
        cursor.execute(query)
        return cursor.fetchall()

    def get_by_id(id):
        statement = "SELECT * FROM products WHERE id=?"
        cursor.execute(statement, [id])
        return cursor.fetchone()

    def insert(photo, description, category, quantity, stock, price, tax):
        statement="INSERT TO products(photo, description, category, quantity, stock, price, tax) VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(statement, [photo, description, category, quantity, stock, price, tax])
        db.commit()
        return True

    def update(id, photo, description, category, quantity, stock, price, tax):
        statement = "UPDATE products SET photo = ? description = ? category = ? quantity = ? stock = ? price = ? tax = ? WHERE id =?"
        cursor.execute(statement, [photo, description, category, quantity, stock, price, tax, id])
        db.commit()
        return True

    def delete(id):
        statement = "DELETE FROM products WHERE id = ?"
        cursor.execute(statement,[id])
        db.commit()
        return True



