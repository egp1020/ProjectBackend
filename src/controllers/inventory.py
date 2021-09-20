from flask import request, render_template, redirect, flash
from flask.views import MethodView
from src.db import cursor

class Inventory(MethodView):
    def get():
        query = "SELECT * FROM invetory"
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_by_id(id):
        statement = "SELECT * FROM inventory WHERE id =?"
        cursor.execute(statement, [id])
        return cursor.fetchone()

    def insert(stock, date_hour):
        statement = "INSERT INTO inventory(stock, date_hour) VALUES (?,?)"
        cursor.execute(statement, [stock, date_hour])
        db.commit()
        return True

    def update(id, stock, date_hour):
        statement = "UPDATE inventory SET stock = ? date_hour = ? WHERE id =?"
        cursor.execute(statement, [stock, date_hour, id])
        db.commit()
        return True

    def delete(id):
        statement = "DELETE FROM inventory WHERE id =?"
        cursor.execute(statement, [id])
        db.commit()
        return True