from flask import Flask
from db import create_tables
from category import category_blueprint


app = Flask(__name__)
app.register_blueprint(category_blueprint)


HOST = 'localhost'
PORT = 4000
DEBUG = True


if __name__ == '__main__':
    create_tables()
    app.run(HOST, PORT, DEBUG)
