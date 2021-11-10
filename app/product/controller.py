from app import db
from .model import ProductModel
from .schema import ProductSchema

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

PRODUCT_NOT_FOUND = "Product not found."
PRODUCT_ALREADY_EXISTS ="Product '{}' already exists."
CATEGORY_NOT_FOUND = "Category not found."

class ProductController:
    def get_product_all(self):
        products = ProductModel.query.all()
        result = products_schema.dump(products)
        return result, 200

    def get_product(self, id):
        product = ProductModel.query.filter_by(id=id).first()
        if product:
            return product_schema.dump(product)
        return {'message': PRODUCT_NOT_FOUND}, 404

    def get_product_category(self, category_id):
        product = ProductModel.query.filter_by(category_id=category_id).all()
        if product:
            return products_schema.dump(product), 200
        return {'message': CATEGORY_NOT_FOUND}, 404

    def insert_product(self, product):
        name = product["name"]
        product_find = ProductModel.query.filter_by(name=name).first()
        if product:
            return {'message': PRODUCT_ALREADY_EXISTS }

        photo_find = product["photo"]
        if not photo_find:
            filename = "No upload img"
        else:
            filename = str(date.today()).replace('-', '') + secure_filename(photo_find.filename)
            photo_find.save(os.getcwd()+"/img" + photo_find.filaname)

        photo = filename
        description = product["description"]
        category = product["category"]
        quantity = product["quantity"]
        price = product["price"]
        tax = product["tax"]
        barcode = product["barcode"]

        new_product = ProductModel(photo, description, category, quantity, price, tax, barcode)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product)

    def updateProduct(self, product, id):
        photo_find = product["photo"]
        if not photo_find:
            filename = "No upload img"
        else:
            filename = str(date.today()).replace('-', '') + secure_filename(photo_find.filename)
            photo_find.save(os.getcwd()+"/img" + photo_find.filaname)

        photo = filename
        description = product["description"]
        category = product["category"]
        quantity = product["quantity"]
        price = product["price"]
        tax = product["tax"]
        barcode = product["barcode"]
        product_id = ProductModel.query.get(id)
        if product_id:
            photo_find.photo = photo
            photo_find.description = description
            photo_find.category_id = category
            photo_find.quantity = quantity
            photo_find.price = price
            photo_find.tax_id = tax
            photo_find.barcode = barcode
            db.session.commit()
            return product_schema.jsonify(product_id)
        return {'message': PRODUCT_NOT_FOUND}, 404


    def deleteProduct(self, id):
        product = ProductModel.query.filter_by(id=id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return product_schema.jsonify(product)
        return {'message':PRODUCT_NOT_FOUND}, 404