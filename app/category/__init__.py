from flask import Blueprint

bpcategory = Blueprint('bpcategory', __name__, template_folder='templates')

from . import routes

