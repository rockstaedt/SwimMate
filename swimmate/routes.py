from flask import render_template, url_for, flash, redirect, request
from swimmate import app, db, bycrypt
from swimmate.forms import LoginForm, RegistrationForm
from swimmate.models import User, Training
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime


@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/trainings")
def trainings():
    return render_template("trainings.html")


@app.route("/save_training", methods=["POST", "GET"])
def save_training():
    date = datetime.strptime(request.form["date"], "%Y-%m-%d")
    training = Training(date_training=date,
                        duration_training=2,
                        distance_training=request.form["distance"],
                        user_id=1)
    db.session.add(training)
    db.session.commit()
    flash("Training saved", "success")
    return redirect(url_for("trainings"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        # generate a hashed password with bycrypt
        hashed_password = bycrypt.generate_password_hash(form.password.data).decode("utf-8")
        # create user
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # add user to database
        db.session.add(user)
        # commit database changes
        db.session.commit()
        # flash message that user has been created
        flash("Your account has been created! You are now able to login.", 'success')
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bycrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check email and password!", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")

