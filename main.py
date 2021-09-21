from flask import render_template as render
from src.db import create_tables
from src import create_app

app = create_app()

@app.route("/")
def index():
    return render('index.html')


HOST = 'localhost'
PORT = 4000
DEBUG = True


if __name__ == '__main__':
    create_tables()
    app.run(HOST, PORT, DEBUG)
