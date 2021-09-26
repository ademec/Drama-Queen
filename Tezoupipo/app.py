from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(dir_path, "templates")
statics = os.path.join(dir_path, "static")

app = Flask(
    "Application",
    template_folder=templates,
    static_folder=statics
)
# On configure la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'
# On initie l'extension
db = SQLAlchemy(app)

from .routes import player, accueil, recherche