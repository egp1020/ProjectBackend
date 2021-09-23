from app import get_db
class tax:
    def __init__(self):
        self.db = get_db()
        self.cursor = get_db().cursor()

    def get():
        query = "SELECT * FROM tax"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(id):
        statement = "SELECT * FROM tax WHERE id =?"
        self.cursor.execute(statement, [id])
        return self.cursor.fetchone()

    def create(taxType, rate):
        statement = "INSERT INTO tax(taxType, rate) VALUES (?,?)"
        self.cursor.execute(statement, [taxType, rate])
        self.db.commit()
        return True

    def update(id, taxType, rate):
        statement = "UPDATE tax SET taxType = ? rate = ? WHERE id =?"
        self.cursor.execute(statement, [taxType, rate, id])
        self.db.commit()
        return True

    def delete(id):
        statement = "DELETE FROM tax WHERE id =?"
        self.cursor.execute(statement, [id])
        self.db.commit()
        return True
