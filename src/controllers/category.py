from flask import request, render_template, redirect, flash
from flask.views import MethodView
from src.db import cursor

class Category(MethodView):
    def get():
        query = "SELECT * FROM category"
        cursor.execute(query)
        return cursor.fetchall()

    def get_by_id(id):
        statement = "SELECT * FROM category WHERE id =?"
        cursor.execute(statement, [id])
        return cursor.fetchone()

    def insert(name, photo, description):
        db = get_db()
        cursor = db.cursor()
        statement = "INSERT INTO category(photo, name, description) VALUES (?,?,?)"
        cursor.execute(statement, [name, photo, description])
        db.commit()
        return True

    def update(id, name, photo, description):
        db = get_db()
        cursor = db.cursor()
        statement = "UPDATE category SET photo = ?, name = ?, description = ? WHERE id =?"
        cursor.execute(statement, [name, photo, description, id])
        db.commit()
        return True

    def delete(id):
        db = get_db()
        cursor = db.cursor()
        statement = "DELETE FROM category WHERE id =?"
        cursor.execute(statement, [id])
        db.commit()
        return True