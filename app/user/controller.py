from app import db
from app.user.model import User

class UserController:
    def getUsers(self):
        users = User.query.all()
        user = []

        for element in users:
            user.append({
                'id':element.id,
                'email':element.email,
                'password':element.password,
                'name':element.name,
                'last_name':element.last_name,
                'phone':element.phone
            })

        return user

    def getUser(self, username):
        users = []
        user = User.query.filter_by(username=username).firts()

        if user is not None:
            users.append({
                'id':user.id,
                'email':user.email,
                'password':user.password,
                'name':user.name,
                'last_name':user.last_name,
                'phone':user.phone
            })
        else:
            users.append({
                'messages':'No se encontro el elemento.'
            })
        return users

    def insertUser(self, user):
            if user is not None:
                email = user["email"]
                password = set_password(user["password"])
                name = user["name"]
                last_name = user["last_name"]
                phone = user["phone"]

                newUser= User(email, password, name, last_name, phone)
                db.session.add(newUser)
                db.session.commit()

                message = {'message': 'registered successfully'}
            else:
                message = {'message': 'registered unccessfully'}
            return message

    def updateUser(self, user, id):
        email = user["email"]
        password = user["password"]
        name = user["name"]
        last_name = user["last_name"]
        phone = user["phone"]

        user_id = User.query.get(id)

        if user is not None:
            user_id.email = email
            user_id.password = set_password(password)
            user_id.name = name
            user_id.last_name = last_name
            user_id.phone = phone
            db.session.commit()
            message = "El registro se actualizo correctamente"
        else:
            message = "La actualización no se pudo realizar con éxito"
        return message


    def deleteUser(self, id):
        user = User.query.filter_by(id=id).first()
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            message = "El usuario se ha sido eliminada con éxito."
        else:
            message = "La usuario no se pudo eliminar."
        return message