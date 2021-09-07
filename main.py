from flask import Flask
from db import create_tables

app = Flask(__name__)

HOST = 'localhost'
PORT = 4000
DEBUG = True

if __name__ == '__main__':
    create_tables()
    app.run(HOST, PORT, DEBUG)
