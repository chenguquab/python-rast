from __future__ import annotations
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/library_flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(20))

@app.route('/process', methods=["POST"])
def process():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    new_member = members(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
    db.session.add(new_member)
    db.session.commit()
    
    return redirect(url_for("table")


@app.route('/form/')
def form():
    return render_template('form.html' )

@app.route('/table')
def table():
    return render_template('table.html' )




























# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))






















# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return f'Subpath {escape(subpath)}'

# @app.route('/test/<str:new>')






# @app.route('/')
# def index():
#     return "Index Page"

# @app.route('/hello')
# def hello():
#     return 'Hello, World'