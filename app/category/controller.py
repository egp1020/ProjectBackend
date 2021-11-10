from app import db
from .model import CategoryModel
from .schema import CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

CATEGORY_NOT_FOUND = "Category not found."
CATEGORY_ALREADY_EXISTS = "Category '{}' already exists."

class CategoryController:
    def get_category_all(self):
        categories = CategoryModel.query.all()
        result = categories_schema.dump(categories)
        return result, 200

    def get_category(self, id):
        category = CategoryModel.query.filter_by(id=id).first()
        if category:
            return category_schema.dump(category)
        return {'message': CATEGORY_NOT_FOUND}, 404

    def insert_category(self, category):
        name = category["name"]
        category_find = CategoryModel.query.filter_by(name=name).first()
        if category_find:
            return {'message': CATEGORY_ALREADY_EXISTS.format(name)}, 400

        photo = category["photo"]
        description = category["description"]
        new_category = CategoryModel(photo, name, description)
        db.session.add(new_category)
        db.session.commit()
        return category_schema.jsonify(new_category)

    def update_category(self, category, id):
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
        return {'message': CATEGORY_NOT_FOUND}, 404

    def delete_category(self, id):
        category = CategoryModel.query.filter_by(id=id).first()
        if category:
            db.session.delete(category)
            db.session.commit()
            return category_schema.jsonify(category)
        return {'message': CATEGORY_NOT_FOUND}, 404

