from flask import render_template, url_for, flash, redirect
from swimmate import app
from swimmate.forms import LoginForm, RegistrationForm
from swimmate.models import User, Training

records = [
    {
        "user": "Eric Rockstädt",
        "type": "Swimming",
        "date": "28.06.2020",
        "time": "15:00",
        "duration": 60,
        "distance": 2.5
    },
    {
        "user": "Eric Rockstädt",
        "type": "Swimming",
        "date": "25.06.2020",
        "time": "14:00",
        "duration": 60,
        "distance": 2
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html", records=records)


@app.route("/about")
def about():
    return "Hello about"


@app.route("/trainings")
def trainings():
    return render_template("trainings.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return url_for("home")
        else:
            flash("Login unsuccessful. Please check username and password!", "danger")
    return render_template("login.html", title="Login", form=form)

