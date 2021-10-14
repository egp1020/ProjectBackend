from app import app
from app import db


HOST = 'localhost'
PORT = 4000
DEBUG = True


if __name__ == '__main__':
    db.create_all()
    app.run(HOST, PORT, DEBUG)
