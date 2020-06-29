from flask import Flask, render_template, url_for

app = Flask(__name__)

trainings = [
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
    return render_template("home.html", trainings=trainings)


@app.route("/about")
def about():
    return "Hello about"


if __name__ == '__main__':
    app.run(debug=True)
