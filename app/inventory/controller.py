from app import app, db
from app.inventory.model import Inventory

class InventoryController:
    def getProductInventoryAll(self):
        products = Inventory.query.all()
        inventory = []

        for element in products:
            inventory.append({
                'id':element.id,
                'product':element.product,
                'stock':element.stock,
                'date_created':element.date_created
            })
        return inventory

    def getProductInventory(self, id):
        products = []
        inventory = Inventory.query.filter_by(id=id).first()

        if inventory is not None:
            products.append({
                'id':inventory.id,
                'product':inventory.product,
                'stock':inventory.stock,
                'date_created':inventory.date_created
            })
        else:
            products.append({
                'message':'no se encontro elemento.',
            })
        return products

    def insertProductInventory(self, new_product):
        if new_product is not None:
            product = new_product["product"]
            stock = new_product["stock"]
            date_created = new_product["date_created"]

            new_inventory = Inventory(product, stock, date_created)
            db.session.add(new_inventory)
            db.session.commit()

            message = "El registro del producto se realizo con éxito."
        else:
            message = "El registro del producto no fue éxitoso."
        return message

    def updateProductInventory(self, old_product, id):
        if old_product is not None:
            product_id = Inventory.query.get(id)
            product = old_product["product"]
            stock = old_product["stock"]
            date_created = old_product["date_created"]

            product_id.product = product
            product_id.stock = stock
            product_id.date_created = date_created
            db.session.commit()
            message = "La actualización del producto se realizo con éxito."
        else:
            message = "El actualización del producto no fue éxitosa."
        return message

    def deleteProductInventory(self, id):
        product = Inventory.query.filter_by(id = id).first()
        if product is not None:
            db.session.delete(product)
            db.session.commit()
            message = "El producto ha sido eliminado con éxito."
        else:
            message = "El producto no se ha podido eliminar."
        return message

