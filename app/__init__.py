from flask import Flask
from flask import render_template as render
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.py')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render('404.html'), 404

from .category import bpcategory
app.register_blueprint(bpcategory)

from .inventory import bpinventory
app.register_blueprint(bpinventory)

from .product import product
app.register_blueprint(bpproduct)

from .tax import bptax
app.register_blueprint(bptax)

from .taxDetails import bptaxDetails
app.register_blueprint(bptaxDetails)