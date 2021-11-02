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