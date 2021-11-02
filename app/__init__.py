import os
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api_v1 import blueprint as api_v1

bdDirectory = f'sqlite:///{os.getcwd()}/database/tables.db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = bdDirectory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
CORS(app)

app.register_blueprint(api_v1)
