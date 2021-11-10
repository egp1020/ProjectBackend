from app import app, db


HOST = 'localhost'
PORT = 5000
DEBUG = True


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(HOST, PORT, DEBUG)
