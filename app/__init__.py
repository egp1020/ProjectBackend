import os
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.middleware.proxy_fix import ProxyFix


bdDirectory = f'sqlite:///{os.getcwd()}/database/tables.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = bdDirectory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.wsgi_app = ProxyFix(app.wsgi_app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from .api_v1 import blueprint as api_v1
app.register_blueprint(api_v1)
