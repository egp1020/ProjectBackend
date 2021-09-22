from flask import Blueprint

bpproduct = Blueprint('bpproduct', __name__, template_folder='templates')

from . import routes