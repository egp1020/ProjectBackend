from db import get_db

def insert(photo, description, category, quantity, stock, price, tax):
    db = get_db()
    cursor = db.cursor()
    statement="INSERT TO products(photo, description, category, quantity, stock, price, tax) VALUES(?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [photo, description, category, quantity, stock, price, tax])
    db.commit()
    return True

def update(id, photo, description, category, quantity, stock, price, tax):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE products SET photo = ? description = ? category = ? quantity = ? stock = ? price = ? tax = ? WHERE id =?"
    cursor.execute(statement, [photo, description, category, quantity, stock, price, tax, id])
    db.commit()
    return True

def delete(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM products WHERE id = ?"
    cursor.execute(statement,[id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM products WHERE id=?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    return cursor.fetchall()