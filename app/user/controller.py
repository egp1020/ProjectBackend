from app import db
from app.user.model import User

class UserController:
    def getUsers(self):
        users = User.query.all()
        user = []

        for element in users:
            user.append({
                'id':element.id,
                'public_id':element.public_id,
                'username':element.username,
                'email':element.email,
                'password':element.password,
                'admin':element
            })

        return user

    def getUser(self, username):
        users = []
        user = User.query.filter_by(username=username).firts()

        for element in user:
            users.append({
                'id':element.id,
                'public_id':element.public_id,
                'username': element.username,
                'email':element.email,
                'password':element.password,
                'admin':element.admin
            })
