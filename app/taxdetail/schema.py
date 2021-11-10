from app import ma
from app.tax.schema import TaxSchema
from .model import TaxDetailModel

class TaxDetailSchema(ma.SQLAlchemyAutoSchema):
    model = TaxDetailModel
    load_instance = True
    include_relationships = True

    tax_relationship = ma.Nested(TaxSchema,)