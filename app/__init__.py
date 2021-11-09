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

from .category.routes import category_app
app.register_blueprint(category_app)

from .product.routes import product_app
app.register_blueprint(product_app)

from .category.routes import category_api
from .inventory.routes import inventory_api
from .product.routes import product_api

api =  Api(app, version="1.0", title="Product management ", description="Manage orders", doc="/doc")

api.add_namespace(category_api)
api.add_namespace(inventory_api)
api.add_namespace(product_api)