from db import get_db


class inventory:
    def __init__(self):
        self.db = get_db()
        self.cursor = get_db().cursor()

    def get():
        query = "SELECT * FROM invetory"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(id):
        statement = "SELECT * FROM inventory WHERE id =?"
        self.cursor.execute(statement, [id])
        return self.cursor.fetchone()

    def insert(stock, date_hour):
        statement = "INSERT INTO inventory(stock, date_hour) VALUES (?,?)"
        self.cursor.execute(statement, [stock, date_hour])
        self.db.commit()
        return True

    def update(id, stock, date_hour):
        statement = "UPDATE inventory SET stock = ? date_hour = ? WHERE id =?"
        self.cursor.execute(statement, [stock, date_hour, id])
        self.db.commit()
        return True

    def delete(id):
        statement = "DELETE FROM inventory WHERE id =?"
        self.cursor.execute(statement, [id])
        self.db.commit()
        return True