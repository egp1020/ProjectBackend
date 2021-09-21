from flask import Blueprint

bpcategory = Blueprint('bpcategory', __name__, template_folder='templates', static_folder='static')

from . import routes

