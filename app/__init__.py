from flask import Flask
from flask import render_template as render
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config.py')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render('404.html'), 404

from app.category import bpcategory
app.register_blueprint(bpcategory)

from app.inventory import bpinventory
app.register_blueprint(bpinventory)

from app.product import product
app.register_blueprint(bpproduct)

from app.tax import bptax
app.register_blueprint(bptax)

from app.taxDetails import bptaxDetails
app.register_blueprint(bptaxDetails)