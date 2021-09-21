from ...src import database


class category:
    def __init__(self):
        self.db = database.db().get_db()
        self.cursor = get_db().cursor()

    def get(self):
        query = "SELECT * FROM category"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(self, id):
        statement = "SELECT * FROM category WHERE id =?"
        self.cursor.execute(statement, [id])
        return self.cursor.fetchone()

    def create(self, name, photo, description):
        statement = "INSERT INTO category(photo, name, description) VALUES (?,?,?)"
        self.cursor.execute(statement, [name, photo, description])
        self.db.commit()
        return True

    def update(self, id, name, photo, description):
        statement = "UPDATE category SET photo = ?, name = ?, description = ? WHERE id =?"
        self.cursor.execute(statement, [name, photo, description, id])
        self.db.commit()
        return True

    def delete(self, id):
        statement = "DELETE FROM category WHERE id =?"
        self.cursor.execute(statement, [id])
        self.db.commit()
        return True
