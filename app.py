from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "c4d269c24985531076eb5020c1c221a5ex"

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


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
