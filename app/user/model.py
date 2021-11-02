from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    username=db.Column(db.String(15), nullable=False, unique=True)
    email=db.Column(db.String(80), nullable=False)
    password=db.Column(db.Text, nullable=False)
    admin=db.Column(db.Boolean)
    orders = db.relationship('Order', backref='client', lazy='dynamic')

    def __init__(self, public_id, username, email, password, admin):
        self.public_id=public_id
        self.username=username
        self.email=email
        self.password=password
        self.admin=admin

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, pwd):
        self.password=generate_password_hash(pwd['password'], method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)