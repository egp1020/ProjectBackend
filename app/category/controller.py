from app import db
from app.category.model import CategoryModel
from app.category.schema import CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

STORE_NOT_FOUND = "Store not found."
STORE_ALREADY_EXISTS = "Store '{}' already exists."

class CategoryController:
    def getCategoryAll(self):
        categories = CategoryModel.query.all()
        result = categories_schema.dump(categories)
        return result, 200

    def getCategory(self, id):
        category = CategoryModel.query.filter_by(id=id).first()
        if category is not None:
            return category_schema.dump(category)
        return {'message': STORE_NOT_FOUND}, 404

    def insertCategory(self, category):
        name = category["name"]
        category_find = CategoryModel.query.filter_by(name=name).first()
        if category_find:
            return {'message': STORE_ALREADY_EXISTS.format(name)}, 400

        photo = category["photo"]
        name = category["name"]
        description = category["description"]
        new_category = CategoryModel(photo, name, description)
        db.session.add(new_category)
        db.session.commit()
        return category_schema.jsonify(new_category)

    def updateCategory(self, category, id):
        photo = category["photo"]
        name = category["name"]
        description = category["description"]
        category_id = CategoryModel.query.get(id)
        if category_id:
            category_id.photo = photo
            category_id.name = name
            category_id.description = description
            db.session.commit()
            return category_schema.jsonify(category_id)
        return {'message': STORE_NOT_FOUND}, 404

    def deleteCategory(self, id):
        category = CategoryModel.query.filter_by(id=id).first()
        if category:
            db.session.delete(category)
            db.session.commit()
            return category_schema.jsonify(category)
        return {'message': STORE_NOT_FOUND}, 404

