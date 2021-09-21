from flask import Flask
from .category import bpcategory
app.register_blueprint(bpcategory)

def create_app():
    app = Flask(__name__)
    return app