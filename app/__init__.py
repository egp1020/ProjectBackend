from flask import Flask
from flask import render_template as render

app = Flask(__name__)

from category.routes import bpcategory
app.register_blueprint(bpcategory)

from inventory.routes import bpinventory
app.register_blueprint(bpinventory)

from product.routes import bpproduct
app.register_blueprint(bpproduct)

from tax.routes import bptax
app.register_blueprint(bptax)

from taxDetails.routes import bptaxDetails
app.register_blueprint(bptaxDetails)