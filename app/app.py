from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
import os
#import pandas as pd
from .models.model import Thesis, db, Response

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
    thesisTrue = Thesis.query.filter(Thesis.isTrue==True).limit(5).all()
    thesisFalse = Thesis.query.filter(Thesis.isTrue==False).limit(5).all()
    thesisTrue.extend(thesisFalse)
    thesis = thesisTrue
    #thesis = Thesis.query.filter(Thesis.isTrue==False).limit(500).union().Thesis.query.filter(Thesis.isTrue==True).limit(500)
    return render_template(
        "pages/tezoupipo.html",
        nom="app",
        thesis=thesis
    )


@app.route("/stats", methods=["GET", "POST"])
def stats():

    return render_template(
        "pages/stats.html",
        nom="stats",
    )


@app.route("/stat", methods=["POST"])
def stat():
    res = request.get_json()
    print(res)
    these = Thesis.query.get(res["id"])
    Response.add_response(these, res["answer"])
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
