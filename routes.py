from flask import render_template, request, redirect, url_for
from app import app, db
from models import Subject, Task, UserSettings
from scheduler import generate_schedule
from datetime import datetime

@app.route("/")
def dashboard():
    subjects = Subject.query.all()
    tasks = Task.query.all()
    completed = sum(1 for t in tasks if t.completed)
    total = len(tasks)
    progress = (completed / total * 100) if total > 0 else 0
    return render_template("dashboard.html", subjects=subjects, tasks=tasks, progress=progress)

@app.route("/add_subject", methods=["POST"])
def add_subject():
    name = request.form.get("name")
    if name:
        db.session.add(Subject(name=name))
        db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    subjects = Subject.query.all()
    if request.method == "POST":
        subject_id = request.form.get("subject")
        difficulty = int(request.form.get("difficulty"))
        deadline = datetime.strptime(request.form.get("deadline"), "%Y-%m-%d").date()
        hours = int(request.form.get("hours"))
        task = Task(subject_id=subject_id, difficulty=difficulty, deadline=deadline, hours=hours)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("add_task.html", subjects=subjects)

@app.route("/generate_schedule")
def generate_schedule_view():
    settings = UserSettings.query.first()
    if not settings:
        return "Please set daily study hours first."
    tasks = Task.query.filter_by(completed=False).all()
    schedule = generate_schedule(tasks, settings.daily_hours)
    return render_template("schedule.html", schedule=schedule)

@app.route("/complete_task/<int:task_id>")
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        db.session.commit()
    return redirect(url_for("dashboard"))
