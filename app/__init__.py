import os
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

bdDirectory = f'sqlite:///{os.getcwd()}/database/tables.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = bdDirectory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
CORS(app)

from .category.routes import bpcategory
app.register_blueprint(bpcategory)

from .inventory.routes import bpinventory
app.register_blueprint(bpinventory)

from .product.routes import bpproduct
app.register_blueprint(bpproduct)

from .tax.routes import bptax
app.register_blueprint(bptax)

from .taxDetails.routes import bptaxdetails
app.register_blueprint(bptaxdetails)