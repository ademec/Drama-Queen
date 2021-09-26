from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
import os

from .models.model import Thesis, db

dir_path = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(dir_path, "templates")
statics = os.path.join(dir_path, "static")

app = Flask(
    __name__,
    template_folder=templates,
    static_folder=statics
)


@app.route("/", methods=["GET", "POST"])
def home():
    thesis = Thesis.query.all()
    # positions = []
    # for these in thesis:
    #     positions.append({"id": these.id, "title": these.title, "isTrue": these.isTrue})

    return render_template(
        "pages/tezoupipo.html",
        nom="app",
        thesis=thesis,
    )


@app.route("/stat", methods=["POST"])
def stat():
    res = request.get_json()
    print(res)
    return jsonify({"response": True})


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data.db'
migrate = Migrate(app, db)


def config_app():
    """ Create the application """
    db.init_app(app)
    db.app = app
    db.create_all()
    return app


if __name__ == "__main__":
    app.config_app()
    app.run(debug=True)
