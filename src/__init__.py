from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .category import bpcategory

app = Flask(__name__)

db = SQLAlchemy(app)
app.register_blueprint(bpcategory)


"""def create_app():
    app = Flask(__name__)
    return app"""