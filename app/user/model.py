from app import db

class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(15), nullable=False, unique=True)
    email=db.Column(db.String(80), nullable=False)
    password=db.Column(db.Text, nullable=False)

    def __init__(self, username, email, password):
        self.username=username
        self.email=email
        self.password=password

    def __repr__(self):
        return f"<User {self.username}>"