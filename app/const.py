from warnings import warn
import os

RESULTS_PER_PAGE = 9

SECRET_KEY = "JE SUIS UN SECRET !"
# variable nécessaire à la création d'applications Flask
# utilisée comme clé cryptographique pour générer des tokens notamment
# elle permet avec Flask-WTForm de protéger l'envoi des données
# lorsque l'utilisateur soumet des formulaires web
API_ROUTE = "/api"

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)

# Les paramètres de configuration de l'application en mode test
# sont définis en tant que variables de classe au sein de la classe _TEST
if os.environ.get('DATABASE_URL') is None:
    class _TEST:
        SECRET_KEY = SECRET_KEY
        # On configure la base de données de test
        SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    # sqlite:// représente le moteur utilisé, ici SQLite
    # puis / signifie ici qu'il s'agit d'un chemin relatif (un chemin absolu avec //)
    # puis le chemin du fichier à aller chercher, en l'occurence db.sqlite
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    class _PRODUCTION:
        SECRET_KEY = SECRET_KEY
        # On configure la base de données de production
        SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
else:
    class _TEST:
        SECRET_KEY = SECRET_KEY
        # On configure la base de données de test
        SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    class _PRODUCTION:
        SECRET_KEY = SECRET_KEY
        # On configure la base de données de production
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        SQLALCHEMY_TRACK_MODIFICATIONS = False

CONFIG = {
    "test": _TEST,
    "production": _PRODUCTION
}
