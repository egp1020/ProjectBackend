from .controller import TaxDetailController

from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource, fields

controller = TaxDetailController()
tax_detail_app = Blueprint('tax_detail_app', __name__, url_prefix='/app/')
tax_detail_api = Namespace('tax_detail_api', description='Tax detail operations', path='/taxdetail/')

tax_detail_schema = tax_detail_api.model('Tax detail', {
    'id':fields.Integer(readonly=True, description='The tax detail unique identifier'),
    'tax_id':fields.Integer('Tax identifier'),
    'amount_buy':fields.Float('Value of buy without tax'),
    'value_tax': fields.Float('Value  of the tax taken from the amount buy.'),
})

@tax_detail_api.route('/')
class TaxDetailList(Resource):
    """Shows a list of all tax detail and lets you POST to add new tax details"""
    @tax_detail_api.doc('list_taxs_details')
    @tax_detail_api.marshal_list_with(tax_detail_schema)
    def get(self):
        """List all taxs details"""
        taxs_details = controller.get_tax_detail_all()
        return jsonify(taxs_details)

    @tax_detail_api.doc('tax_detail_category')
    @tax_detail_api.expect(tax_detail_schema)
    @tax_detail_api.marshal_list_with(tax_detail_schema, code=201)
    def post(self):
        """Creates a new tax detail"""
        tax_detail = {
            'tax_type': request.json["tax_type"],
            'amount_buy': request.json["amount_buy"],
            'base_buy': request.json["base_buy"],
            'value_tax': request.json["value_tax"]
        }

        new_tax_detail = controller.insert_tax_detail(tax_detail)
        return new_tax_detail

@tax_detail_api.route("/<int:id>")
@tax_detail_api.response(202, "OK")
@tax_detail_api.response(404, "Tax detail not found")
@tax_detail_api.response(404, "Mapping Key Error")
@tax_detail_api.param("id", "The tax detail identifier")
class TaxDetail(Resource):
    @tax_detail_api.doc('get_tax_detail')
    @tax_detail_api.marshal_list_with(tax_detail_schema)
    def get(self, id):
        """Lists of all tax detail  for a particular buy"""
        tax_detail = controller.get_tax_detail(id)
        return jsonify(tax_detail)

    @tax_detail_api.doc('update_tax_detail')
    @tax_detail_api.expect(tax_detail_schema)
    @tax_detail_api.marshal_list_with(tax_detail_schema)
    def update(self, id):
        """Update a tax detail given its identifier"""
        tax_detail = {
            'tax_type': request.json["tax_type"],
            'amount_buy': request.json["amount_buy"],
            'base_buy': request.json["base_buy"],
            'value_tax': request.json["value_tax"]
        }

        tax_detail_update = controller.update_tax_detail(tax_detail, id)
        return tax_detail_update

    @tax_detail_api.doc('dalete_tax_detail')
    @tax_detail_api.expect(tax_detail_schema)
    @tax_detail_api.response(204, "Tax detail deleted")
    def delete(self, id):
        tax_detail = controller.delete_tax(id)
        return tax_detail, 204