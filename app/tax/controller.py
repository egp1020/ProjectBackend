from app import db
from .model import TaxModel
from .schema import TaxSchema

tax_schema = TaxSchema()
taxs_schema = TaxSchema(many=True)

TAX_NOT_FOUND = "Tax not found."
TAX_ALREADY_EXISTS = "Tax '{}' already exists."

class TaxController:
    def get_tax_all(self):
        taxs = TaxModel.query.all()
        result = tax_schema.dump(taxs)
        return result, 200

    def get_tax(self, id):
        tax = TaxModel.query.filter_by(id=id).first()
        if tax:
            return tax_schema.dump(tax)
        return {'message': TAX_NOT_FOUND}, 404

    def insert_tax(self, tax):
        rate = tax["rate"]
        if rate:
            return {'message':TAX_ALREADY_EXISTS}, 400

        tax_type = tax["tax_type"]
        new_tax = TaxModel(tax_type, rate)
        db.session.add(new_tax)
        db.session.commit()
        return tax_schema.jsonify(new_tax)

    def update_tax(self, tax, id):
        tax_type = tax["tax_type"]
        rate = tax["rate"]
        tax_id = TaxModel.query.get(id)
        if tax_id:
            tax_id.tax_type = tax_type
            tax_id.rate = rate
            db.session.commit()
            return tax_schema.jsonify(tax_id)
        return {'message': TAX_NOT_FOUND}, 404


    def deleteTax(self, id):
        tax = TaxModel.query.filter_by(id=id).first()
        if tax:
            db.session.delete(tax)
            db.session.commit()
            return tax_schema.jsonify(tax)
        return {'message':TAX_NOT_FOUND}, 404