from app import ma
from .model import CategoryModel
from app.product.schema import ProductSchema

class CategorySchema(ma.SQLAlchemyAutoSchema):
    products = ma.Nested(ProductSchema, many=True)
    class Meta:
        model = CategoryModel
        load_instance = True
        include_fk = True

    """ id = ma.auto_field()
    photo = ma.auto_field()
    name = ma.auto_field()
    description = ma.auto_field() """