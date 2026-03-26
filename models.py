from app import db

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)  # 1-5 scale
    deadline = db.Column(db.Date, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    subject = db.relationship('Subject', backref=db.backref('tasks', lazy=True))

class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    daily_hours = db.Column(db.Integer, nullable=False)
