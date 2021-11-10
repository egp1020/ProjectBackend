from app import db
from .model import TaxDetailModel
from .schema import TaxDetailSchema

tax_detail_schema = TaxDetailSchema()
taxs_details_schema = TaxDetailSchema(many=True)


TAX_DETAIL_NOT_FOUND = "Tax not found."
TAX_DETAIL_ALREADY_EXISTS = "Tax '{}' already exists."


class TaxDetailController:
    def get_tax_detail_all(self):
        taxs_details = TaxDetailModel.query.all()
        result = taxs_details_schema.dump(taxs_details)
        return result

    def get_tax_detail(self, id):
        tax_detail = TaxDetailModel.query.filter_by(id=id).first()

        if tax_detail:
            return tax_detail_schema.dump(tax_detail)
        return {'message': TAX_DETAIL_NOT_FOUND}, 404

    def insert_tax_detail(self, tax_detail):
        tax_id = tax_detail["tax_id"]
        amount_buy = tax_detail["amount_buy"]
        base_buy = tax_detail["base_buy"]
        value_tax = tax_detail["value_tax"]

        new_tax_detail = TaxDetailModel(tax_id, amount_buy, base_buy, value_tax)
        db.session.add(new_tax_detail)
        db.session.commit()
        return tax_detail.jsonify(new_tax_detail)

    def update_tax_detail(self, tax_detail, id):
        tax_type = tax_detail["tax_type"]
        amount_buy = tax_detail["amount_buy"]
        base_buy = tax_detail["base_buy"]
        value_tax = tax_detail["value_tax"]
        tax_detail_id = TaxDetailModel.query.filter_by(id = id).first()
        if tax_detail_id:
            tax_detail_id.tax_type = tax_type
            tax_detail_id.amount_buy = amount_buy
            tax_detail_id.base_buy = base_buy
            tax_detail_id.value_tax = value_tax
            db.session.commit()
            return tax_detail_schema.jsonify(tax_detail_id)
        return {'message':TAX_DETAIL_NOT_FOUND}, 404


    def delete_tax(self, id):
        tax_detail = TaxDetailModel.query.filter_by(id=id).first()
        if tax_detail:
            db.session.delete(tax_detail)
            db.session.commit()
            return tax_detail_schema.jsonify(tax_detail)
        return {'message':TAX_DETAIL_NOT_FOUND}, 404