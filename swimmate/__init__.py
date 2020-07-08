from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "c4d269c24985531076eb5020c1c221a5ex"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

from swimmate import routes
