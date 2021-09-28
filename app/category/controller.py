from model import Category
from sqlalchemy import or_

class CategoryController:
    def getCategoryAll(self):
        categories = category.query.all()
        category = []

        for line in categories:
            category.append({
                'id':line.id,
                'photo':line.photo,
                'name':line.name,
                'description':line.description
            })
        return category

    def getCategory(self, id):
        categories = []
        category = Category.query.filter_by(id=id).first()

        if category is not None:
            categories.append({
                'id':category.id,
                'photo':category.photo,
                'name':category.name,
                'description':category.description
            })
        else:
            categories.append({
                'messages':'no se encontro id.',
            })
        return categories

    def insertCategory(self, category):
        photo = category["photo"]
        name = category["name"]
        description = category["description"]
