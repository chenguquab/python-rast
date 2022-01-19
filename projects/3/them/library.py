from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/flask_library"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(100))
    last = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.Integer)

db.create_all()
db.session.commit()

@app.route("/")
def index():
    members = Member.query.all()
    return render_template("index.html", members=members)

@app.route("/new")
def new():
    return render_template("form.html", form_action='insert', member=None)

@app.route("/insert", methods=["POST"])
def insert():
    first = request.form["first"]
    last = request.form["last"]
    email = request.form["email"]
    phone = request.form["phone"]

    member = Member(first=first, last=last, email=email, phone=phone)
    db.session.add(member)
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/edit/<id>")
def edit(id):
    member = Member.query.get(id)
    return render_template("form.html", member=member, form_action='update')


@app.route("/update", methods=["POST"])
def update():
    first = request.form["first"]
    last = request.form["last"]
    email = request.form["email"]
    phone = request.form["phone"]
    id = request.form["id"]

    member = Member.query.get(id)

    member.first = first
    member.last = last
    member.email = email
    member.phone = phone
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/delete/<id>")
def delete(id):
    member = Member.query.get(id)
    db.session.delete(member)
    db.session.commit()
    
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)