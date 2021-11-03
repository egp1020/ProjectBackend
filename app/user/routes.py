import uuid
import datetime
from flask import request, jsonify, make_response
from app import app, db
from .model import set_password, check_password

@app.route('/register', methods=['GET', 'POST'])
def signup_user():
    data = request.get_json()
    hashed_password = set_password(data)

    new_user = Users(public_id=str(uuid.uuid4()), username=data['name'], email=data['email'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'registered successfully'})

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

    user = Users.query.filter_by(username=auth.username).first()
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

@app.route('/users', methods=['GET'])
def get_all_users():

    users = Users.query.all()

    result = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        result.append(user_data)

    return jsonify({'users': result})

@app.route('/order', methods=['POST', 'GET'])
@token_required
def create_order(current_user):

    data = request.get_json()

    new_authors = Authors(name=data['name'], country=data['country'], book=data['book'], booker_prize=True, user_id=current_user.id)  
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