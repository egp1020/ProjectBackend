import os
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix


bdDirectory = f'sqlite:///{os.getcwd()}/database/tables.db'

app = Flask(__name__)
app.config['SECRET_KEY']='Th1s1ss3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = bdDirectory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.wsgi_app = ProxyFix(app.wsgi_app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
#login = LoginManager(app)
CORS(app)

@app.before_first_request
def create_tables():
    db.create_all()

""" @app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400 """

#api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api =  Api(app, version="1.0", title="Product management ", description="Manage orders", doc="/doc/")

from .category.routes import category_api
api.add_namespace(category_api)

from .product.routes import product_api
api.add_namespace(product_api)

from .inventory.routes import inventory_api
api.add_namespace(inventory_api)

from .tax.routes import tax_api
api.add_namespace(tax_api)

from .taxdetail.routes import tax_detail_api
api.add_namespace(tax_detail_api)






