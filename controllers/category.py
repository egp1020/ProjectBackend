from db import get_db


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


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM category WHERE id =?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM category"
    cursor.execute(query)
    return cursor.fetchall()
