from datetime import datetime
from swimmate import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    trainings = db.relationship("Training", backref="user", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_training = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration_training = db.Column(db.Integer, nullable=False)
    distance_training = db.Column(db.FLOAT, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Training('{self.date_training}', '{self.duration_training}', '{self.distance_training}')"