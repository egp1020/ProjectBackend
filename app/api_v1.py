from flask_restx import Api
from flask import Blueprint

from category.routes import api as category_api
from inventory.routes import api as inventory_api
from product.routes import api as product_api
from tax.routes import api as tax_api
from taxDetails.routes import api as taxDetails_api

blueprint = Blueprint('api', __name__, url_prefix='/api/')
api =  Api(blueprint, doc='/docs', version="1.0", title="Product management ", description="Manage orders")

api.add_namespace(category_api)
api.add_namespace(inventory_api)
api.add_namespace(product_api)
api.add_namespace(tax_api)
api.add_namespace(taxDetails_api)