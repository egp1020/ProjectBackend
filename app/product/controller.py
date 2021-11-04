from app import app, db
from app.product.model import ProductModel

class ProductController:
    def getProductAll(self):
        products = ProductModel.query.all()
        product = []

        for element in products:
            product.append({
                'id':element.id,
                'photo':element.photo,
                'description':element.description,
                'category':element.category_id,
                'quantity':element.quantity,
                'stock':element.inventory_id,
                'price':element.price,
                'tax':element.tax_id,
                'barcode':element.barcode
            })
        return product

    def getProduct(self, id):
        products = []
        product = ProductModel.query.filter_by(id=id).first()

        if product is not None:
            products.append({
                'photo':product.photo,
                'description':product.description,
                'category':product.category_id,
                'quantity':product.quantity,
                'stock':product.inventory_id,
                'price':product.price,
                'tax':product.tax_id,
                'barcode':product.barcode
            })
        else:
            products.append({
                'messages':'no se encontro id.',
            })
        return products
    
    def getProductCategory(self, category_id):
        products = []
        product = ProductModel.query.filter_by(category_id=category_id).all()

        for element in product:
            products.append({
                'photo':element.photo,
                'description':element.description,
                'category':element.category_id,
                'quantity':element.quantity,
                'stock':element.inventory_id,
                'price':element.price,
                'tax':element.tax_id,
                'barcode':element.barcode
            })
        return products

    def insertProduct(self, product):
        if product is not None:
            photo = product["photo"]
            if not photo:
                filename = "No upload img"
            else:
                filename = str(date.today()).replace('-', '') + secure_filename(photo.filename)
                photo.save(os.getcwd()+"/img" + photo.filaname)

            photo = filename
            description = product["description"]
            category = product["category"]
            quantity = product["quantity"]
            stock = product["stock"]
            price = product["price"]
            tax = product["tax"]
            barcode = product["barcode"]

            data = ProductModel(photo, description, category, quantity, stock, price, tax, barcode)
            db.session.add(data)
            db.session.commit()

            message = "El registro se hizo con éxito"
        else:
            message = "El registro no se logro."
        return message

    def updateProduct(self, product, id):
        photo = product["photo"]
        if not photo:
            filename = "No upload img"
        else:
            filename = str(date.today()).replace('-', '') + secure_filename(photo.filename)
            photo.save(os.getcwd()+"/img" + photo.filaname)

        photo = filename
        description = product["description"]
        category = product["category"]
        quantity = product["quantity"]
        stock = product["inventory"]
        price = product["price"]
        tax = product["tax"]
        barcode = product["barcode"]

        product = ProductModel.query.get(id)
        if product is not None:
            product.photo = photo
            product.description = description
            product.category_id = category
            product.quantity = quantity
            product.inventory_id = stock
            product.price = price
            product.tax_id = tax
            product.barcode = barcode
            db.session.commit()
            message = "El producto se actualizo correctamente"
        else:
            message = "La actualización no se pudo realizar con éxito"
        return message


    def deleteProduct(self, id):
        product = ProductModel.query.filter_by(id=id).first()
        if product is not None:
            db.session.delete(product)
            db.session.commit()
            message = "El producto ha sido eliminado con éxito."
        else:
            message = "El producto no se pudo eliminar."
        return message