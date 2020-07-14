from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    date_create = db.Column(db.DateTime, default=datetime.now())


@app.route("/")
def hello():
    student = Student.query.all()
    return render_template('index.html', data=student)


@app.route("/student/delete/<id>", methods=['GET'])
def delete(id):
    Student.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/')


@app.route("/student")
def studnet():
    return render_template('addstudent.html')


@app.route("/student/add/<name>")
def index(name):
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()

    return "Add User"


@app.route("/update", methods=['POST'])
def update():
    if request.method == "POST":
        row_id = request.form['id']
        name = request.form['fname']
        phone = request.form['phone']

        if name and phone:
            student = Student.query.filter_by(
                id=row_id).first()
            student.name = name
            student.phone = phone
            db.session.commit()
            return redirect('/')
        else:
            flash("Create Fail!")
            return redirect(url_for('studnet'))


@app.route("/insert", methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.form['fname']
        phone = request.form['phone']
        if name and phone:
            student = Student(name=name, phone=phone)
            db.session.add(student)
            db.session.commit()
            return redirect('/')
        else:
            flash("Create Fail!")
            return redirect(url_for('studnet'))


@app.route("/student/get/<name>")
def get_student(name):
    list_html = ''
    student = Student.query.filter_by(name=name).all()
    if student:
        for i in student:
            list_html = list_html + f"<h1>The Student is {i.name}</h1>"
        return list_html
    else:
        return "<h1>Not Student Name</h1>"


if __name__ == "__main__":
    db.create_all()
    # manager.run()
    app.run(debug=True)
