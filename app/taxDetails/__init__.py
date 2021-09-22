from flask import Blueprint

bptaxDetails = Blueprint('bptaxDetails', __name__, template_folder='templates')

from . import routes