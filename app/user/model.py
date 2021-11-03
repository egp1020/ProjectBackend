from app import db, login
from flask_login import UserMixin

import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__="user"
    user_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(100), nullable=False, unique=True)
    last_name =  db.Column(db.String(100), nullable=False, unique=True)
    phone =  db.Column(db.String(60), nullable=False, unique=True)
    address =  db.Column(db.String(150))
    date_of_birth = db.Column(db.Time)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    #admin=db.Column(db.Boolean)

    def __init__(self, email, password, name, last_name,
                    phone, address=None, date_of_birth=None): #admin
        self.public_id=srt(uuid.uuid4())
        self.name=name
        self.email=email.lower()
        self.password=password
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.date_of_birth=date_of_birth
        #self.admin=admin

    def __repr__(self):
        return f"<User {self.name}>"

    def set_password(self, pwd):
        self.password=generate_password_hash(pwd, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)