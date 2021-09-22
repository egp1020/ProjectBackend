from flask import render_template as render
from flask import Flask
from flask import url_for


app = Flask(__name__)

posts = []

@app.route("/")
def home():
    return render('index.html', num_posts=len(posts))

@app.route("/<string:slug>/")
def categories(slug):
    return render("category.html", slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render("inventory.html", post_id=post_id)

@app.route("/sing-up/", methods=["GET", "POST"])
def singUp():
    return render("formulario_category.html")


HOST = 'localhost'
PORT = 4000
DEBUG = True


if __name__ == '__main__':
    #create_tables()
    app.run(HOST, PORT, DEBUG)
