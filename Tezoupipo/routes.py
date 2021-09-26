from flask import render_template, request


from .app import app
from .models.model import Player


@app.route("/")
def accueil():
    # On a bien sûr aussi modifié le template pour refléter le changement
    videos = Player.query.all()
    return render_template("pages/accueil.html", nom="Tezoupipo", videos=videos)


@app.route("/player/<RNO>")
def player(RNO):
    # On a bien sûr aussi modifié le template pour refléter le changement
    unique_video = Player.query.get(RNO)
    return render_template("pages/player.html", nom="Tezoupipo", video=unique_video)

@app.route("/galerie")
def galerie():
    videos = Player.query.all()
    return render_template('pages/galerie.html', nom="Tezoupipo", videos=videos)