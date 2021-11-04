from app import app, db
from .model import check_password
from .controller import UserController

from flask import request, jsonify, make_response

import uuid
import datetime

controller = UserController()

@app.route('/register', methods=['GET', 'POST'])
def signup_user():
    user = {
        'id':request.json["id"],
        'email':request.json["email"],
        'password':request.json["password"],
        'name':request.json["name"],
        'last_name':request.json["last_name"],
        'phone':request.json["phone"]
    }
    newUser = controller.insertUser(user)

    return newUser

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    auth = request.authorization
    user = controller.loginUser(auth)
    return user

@app.route('/users', methods=['GET'])
def get_all_users():
    users = controller.getUsers()
    return jsonify({'users': users})

@app.route('/order', methods=['POST', 'GET'])
@token_required
def create_order(current_user):

    data = request.get_json()

    new_order = Order(name=data['name'], country=data['country'], book=data['book'], booker_prize=True, user_id=current_user.id)
    db.session.add(new_authors)
    db.session.commit()

    return jsonify({'message' : 'new order created'})

@app.route('/authors', methods=['POST', 'GET'])
@token_required
def get_orders(current_user):

    authors = Authors.query.filter_by(user_id=current_user.id).all()

    output = []
    for author in authors:

            author_data = {}
            author_data['name'] = author.name
            author_data['book'] = author.book
            author_data['country'] = author.country
            author_data['booker_prize'] = author.booker_prize
            output.append(author_data)

    return jsonify({'list_of_authors' : output})

@app.route('/authors/<author_id>', methods=['DELETE'])
@token_required
def delete_author(current_user, author_id):
    author = Author.query.filter_by(id=author_id, user_id=current_user.id).first()
    if not author:
        return jsonify({'message': 'author does not exist'})


    db.session.delete(author)
    db.session.commit()

    return jsonify({'message': 'Author deleted'})