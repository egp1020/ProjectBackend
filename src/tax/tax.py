from db import get_db

def insert(taxType, description):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO tax(taxType, description) VALUES (?,?)"
    cursor.execute(statement, [taxType, description])
    db.commit()
    return True

def update(id, taxType, description):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE tax SET taxType = ? description = ? WHERE id =?"
    cursor.execute(statement, [taxType, description, id])
    db.commit()
    return True

def delete(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM tax WHERE id =?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM tax WHERE id =?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM tax"
    cursor.execute(query)
    return cursor.fetchall()