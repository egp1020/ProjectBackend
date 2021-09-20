from db import get_db

def insert(stock, date_hour):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO inventory(stock, date_hour) VALUES (?,?)"
    cursor.execute(statement, [stock, date_hour])
    db.commit()
    return True

def update(id, stock, date_hour):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE inventory SET stock = ? date_hour = ? WHERE id =?"
    cursor.execute(statement, [stock, date_hour, id])
    db.commit()
    return True

def delete(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM inventory WHERE id =?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM inventory WHERE id =?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM invetory"
    cursor.execute(query)
    return cursor.fetchall()