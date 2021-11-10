from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource, fields

from .controller import TaxController

controller = TaxController()
tax_app = Blueprint('tax_app', __name__, url_prefix='/app/')
tax_api = Namespace('tax_api', description='Tax operations', path='/tax/')

tax_schema = tax_api.model('Tax', {
    'id':fields.Integer(readonly=True, description='The tax unique identifier'),
    'tax_type':fields.String('Name of the tax type'),
    'rate': fields.Float('Value of the tax')
})

@tax_api.route('/')
class TaxList(Resource):
    """Shows a list of all categories and lets you POST to add new tags"""
    @tax_api.doc('list_tax')
    @tax_api.marshal_list_with(tax_schema)
    def get(self):
        """List all categories"""
        taxs = controller.get_tax_all()
        return jsonify(taxs)

    @tax_api.doc('create_tax')
    @tax_api.expect(tax_schema)
    @tax_api.marshal_list_with(tax_schema, code=201)
    def post(self):
        """Creates a new tax"""
        tax = {
            'tax_type': request.json["tax_type"],
            'rate': request.json["rate"]
        }
        new_tax = controller.insert_tax(tax)


@tax_api.route("/<int:id>")
@tax_api.response(202, "OK")
@tax_api.response(404, "Tax not found")
@tax_api.response(404, "Mapping Key Error")
@tax_api.param("id", "The tax identifier")
class Tax(Resource):
    @tax_api.doc('get_tax')
    @tax_api.marshal_list_with(tax_schema)
    def get(id):
        tax = controller.get_tax(id)
        return jsonify(tax)


    @tax_api.doc('update_tax')
    @tax_api.expect(tax_schema)
    @tax_api.marshal_list_with(tax_schema)
    def update(id):
        """Update a tax given its identifier"""
        tax = {
            'tax_type': request.json["tax_type"],
            'rate': request.json["rate"]
        }
        taxs = controller.update_tax(tax, id)
        return taxs

    @tax_api.doc('dalete_tax')
    @tax_api.expect(tax_schema)
    @tax_api.response(204, "Tax deleted")
    def delete(id):
        """Deletes a specific tax"""
        tax = controller.delete_tax(id)
        return tax, 204