from flask import Blueprint

bpinventory = Blueprint('bpinventory', __name__, template_folder='templates')

from . import routes