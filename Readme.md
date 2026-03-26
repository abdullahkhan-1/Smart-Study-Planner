# AI Smart Study Planner

A Flask-based web app that generates optimized study schedules using AI heuristics.

## Features
- Add subjects and tasks
- Define daily study hours
- AI scheduling engine
- Weekly timetable visualization
- Progress tracking

## Tech Stack
- Backend: Flask + SQLite
- Frontend: HTML, CSS, JS
- Styling: Bootstrap/Tailwind optional

## Setup
```bash
git clone <repo>
cd AI-Smart-Study-Planner
pip install -r requirements.txt
python
>>> from app import db
>>> db.create_all()
exit()
python app.py
