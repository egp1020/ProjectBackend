from app import db
from app.user.model import User
from .model import check_password

class UserController:
    def getUsers(self):
        users = User.query.all()
        result = []

        for element in users:
            user_data = {
                'id':element.id,
                'public_id':element.public_id,
                'email':element.email,
                'password':element.password,
                'name':element.name,
                'last_name':element.last_name,
                'phone':element.phone
            }
            result.append(user_data)

        return user

    def getUser(self, authEmail):
        users = []
        user = User.query.filter_by(email=authEmail).first()

        if user is not None:
            users.append({
                'id':user.id,
                'public_id':user.public_id,
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

                newUser = User(email, password, name, last_name, phone)
                db.session.add(newUser)
                db.session.commit()

                message = {'message': 'registered successfully'}
            else:
                message = {'message': 'registered unccessfully'}
            return message

    def updateUser(self, user, id, pwd):
        name = user["name"]
        last_name = user["last_name"]
        phone = user["phone"]
        address = user["address"]

        user_id = User.query.get(id)
        if user is not None:
            user_id.name = name
            user_id.last_name = last_name
            user_id.phone = phone
            user_id.address = address
            db.session.commit()
            message = {'message': 'Updated successfully'}
        else:
            message = {'message': 'Update unccessfully'}
        return message


    def deleteUser(self, id, pwd):
        user = User.query.get(id)
        if user is not None and check_password(pwd):
            db.session.delete(user)
            db.session.commit()
            message = "El usuario se ha sido eliminado con éxito."
        else:
            message = "La usuario no se pudo eliminar."
        return message

    def loginUser(self, auth):
        if not auth or not auth.email or not auth.password:
            return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        user = self.getUser(auth.email)[0]
        if check_password(user.password, auth.password):
            token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token' : token.decode('UTF-8')})

        return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})