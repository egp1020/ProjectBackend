# IMPORTAR BASE DE DATOS


class taxDetails:
    def __init__(self):
        self.db = get_db()
        self.cursor = get_db().cursor()

    def get():
        query = "SELECT * FROM taxDetails"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(id):
        statement = "SELECT * FROM taxDetails WHERE id =?"
        self.cursor.execute(statement, [id])
        return self.cursor.fetchone()

    def create():
        statement = "INSERT INTO taxDetails(taxType, amountBuy, baseBuy, valueTax) VALUES (?,?)"
        self.cursor.execute(statement, [taxType, amountBuy, baseBuy, valueTax])
        self.db.commit()
        return True

    def update(id, taxType, amountBuy, baseBuy, valueTax):
        statement = "UPDATE taxDetails SET taxType = ? amountBuy = ? baseBuy = ? valueTax = ? WHERE id =?"
        self.cursor.execute(statement, [taxType, amountBuy, baseBuy, valueTax, id])
        self.db.commit()
        return True

    def delete(id):
        statement = "DELETE FROM taxDetails WHERE id =?"
        self.cursor.execute(statement, [id])
        self.db.commit()
        return True