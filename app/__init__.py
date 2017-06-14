from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate our app and load configuration
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import views, models
