from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)

# Import routes after db initialization
import routes

if __name__ == "__main__":
    app.run(debug=True)
