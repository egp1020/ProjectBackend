from flask import jsonify, request
from product import bpproduct

@bpproduct.route('/products/', methods=["GET"])
def get():
    product = product().get()