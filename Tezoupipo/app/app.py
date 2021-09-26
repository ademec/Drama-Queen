from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from .models.model import Thesis

dir_path = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(dir_path, "templates")
statics = os.path.join(dir_path, "static")

app = Flask(
    __name__,
    template_folder=templates,
    static_folder=statics
)


@app.route("/", methods=["GET", "POST"])
def accueil():
    thesis = Thesis.query.all()
    return render_template(
        "pages/tezoupipo.html",
        nom="app",
        thesis=thesis,
    )


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data.db'
# On initie l'extension
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def config_app():
    """ Create the application """
    db.init_app(app)
    return app


if __name__ == "__main__":
    app.run()
