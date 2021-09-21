from src.db import get_db


class category:
    def __init__(self):
        self._db = get_db()
        self.cursor = get_db().cursor()

    def create(self, name, photo, description):
        statement = "INSERT INTO category(photo, name, description) VALUES (?,?,?)"
        self.cursor.execute(statement, [name, photo, description])
        self._db.commit()
        return True

    def update(self, id, name, photo, description):
        statement = "UPDATE category SET photo = ?, name = ?, description = ? WHERE id =?"
        self.cursor.execute(statement, [name, photo, description, id])
        self._db.commit()
        return True

    def delete(self, id):
        statement = "DELETE FROM category WHERE id =?"
        self.cursor.execute(statement, [id])
        self._db.commit()
        return True

    def get_by_id(self, id):
        statement = "SELECT * FROM category WHERE id =?"
        self.cursor.execute(statement, [id])
        return self.cursor.fetchone()

    def get(self):
        query = "SELECT * FROM category"
        self.cursor.execute(query)
        return self.cursor.fetchall()
