from app import app, db
import os


HOST = 'localhost'
PORT = 5000
DEBUG = True


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    db.session.commit()
    app.run(HOST, PORT, DEBUG)
