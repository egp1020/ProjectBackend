from flask import Flask
from src.db import create_tables
from src.routes.category import bpcategory


app = Flask(__name__)
app.register_blueprint(bpcategory)


HOST = 'localhost'
PORT = 4000
DEBUG = True


if __name__ == '__main__':
    create_tables()
    app.run(HOST, PORT, DEBUG)
