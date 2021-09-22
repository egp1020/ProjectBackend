# IMPORTAR BASE DE DATOS


class product:
    def __init__(self):
        self.db = get_db()
        self.cursor = get_db().cursor()

    def get():
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_by_id(id):
        statement = "SELECT * FROM products WHERE id=?"
        self.cursor.execute(statement, [id])
        return self.cursor.fetchone()

    def insert(photo, description, category, quantity, stock, price, barcode, tax):
        statement = "INSERT TO products(photo, description, category, quantity, stock, price, barcode, tax) VALUES(?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(statement, [photo, description, category, quantity, stock, price, barcode, tax])
        self.db.commit()
        return True

    def update(id, photo, description, category, quantity, stock, price, tax):
        statement = "UPDATE products SET photo = ? description = ? category = ? quantity = ? stock = ? price = ? barcode = ? tax = ? WHERE id =?"
        self.cursor.execute(statement, [photo, description, category, quantity, stock, price, barcode, tax, id])
        self.db.commit()
        return True

    def delete(id):
        statement = "DELETE FROM products WHERE id = ?"
        self.cursor.execute(statement, [id])
        self.db.commit()
        return True
