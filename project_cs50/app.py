import os

from cs50 import SQL
from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(245)
db = SQL("sqlite:///project.db")

db.execute("""CREATE TABLE IF NOT EXISTS users(
           id INTEGER PRIMARY KEY,
           username TEXT NOT NULL,
           password_hash TEXT NOT NULL
           )
           """)

@app.route("/")
def index():
    if "user_id" in session:
        return render_template("calculate.html")
    else:
        return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":

        if not request.form.get("username"):
            return render_template("login.html")

        elif not request.form.get("password"):
            return render_template("login.html")

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["password_hash"], request.form.get("password")):
            return render_template("login.html", apology="Must provide password")
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            flash("No username has been provided")
            return render_template("register.html")

        if not password:
            flash("Enter password please!")
            return render_template("register.html")

        if not confirmation:
            flash("Confirmation is needed")
            return render_template("register.html")

        if password != confirmation:
            print("Password doesn't match")
            return render_template("register.html")

        password_hash = generate_password_hash(password)

        try:
            session["user_id"] = db.execute(
                "INSERT INTO users (username,password_hash) VALUES(?,?)", username, password_hash)
        except db.IntegrityError:
            flash("The username already exists")
            return render_template("register.html")
        return redirect("/login")
    else:
        return render_template("register.html")

@app.route("/calculate", methods=["POST"])
def calculate():

    grades = request.form.getlist("grades[]")

    grades = [float(grade) for grade in grades]
    total_marks = sum(grades)

    if grades:
        percentage = (total_marks / (100 * len(grades))) * 100
    else:
        percentage = 0

    return render_template("calculate.html", percentage=percentage)


@app.route('/Computers.html', methods=['GET', 'POST'])
def computers():
    return render_template('/quizzes/Computers.html')

@app.route("/Maths.html", methods=["GET", "POST"])
def maths():
    return render_template("/quizzes/Maths.html")

@app.route("/English.html", methods=["GET", "POST"])
def english():
    return render_template("/quizzes/English.html")

@app.route("/quizzes/<quiz_name>", methods=["POST"])
def check_answers(quiz_name):
    correct_answers = {
        'answer': 'Logical Value',
        'answers1': 'Progarmming language',
        'answers2': 'Cascading Style Sheets',
        'answers3': 'Javascript',
        'answers4': 'Bubble Sort',
        'answers5': 'Yellow',
        'answers6': 'Password Manager',
        'answers7': 'End-to-end Encryption',
        'answers8': 'High Level',
        'answers9': 'Internal Server Error',
        'answer10': 'Integral',
        'answers11': 'F3',
        'answers12': 'Integral2',
        'answers13': 'cos4',
        'answers14': 'Integration2',
        'answers15': 'pi1',
        'answers16': 'sinx4',
        'answers17': 'degree4',
        'answers18': 'poly1',
        'answers19': 'optimization1',
        'answer20': 'to be',
        'answers21': 'economic',
        'answers22': 'all',
        'answers23': 'to',
        'answers24': 'to be held',
        'answers25': 'be leaked',
        'answers26': 'despite',
        'answers27': 'an',
        'answers28': 'distinguished',
        'answers29': 'fascination',
    }

    score = 0
    for input_name, correct_answer in correct_answers.items():
        selected_answer = request.form.get(input_name)

        if selected_answer == correct_answer:
            score += 1
    return render_template('/quizzes/results.html', score=score)



