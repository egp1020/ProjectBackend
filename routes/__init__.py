from flask import Blueprints
from flask_restx import Api
from resource.category import category

bpcategory = Blueprints("api",__name__)
api = Api(bpcategory, title="category", description="api de categorías", prefix="/categories")