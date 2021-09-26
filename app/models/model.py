from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

PersonThesis = db.Table('person_thesis',
                        db.Column('personid', db.Integer, db.ForeignKey('person.personid'), primary_key=True),
                        db.Column('thesisid', db.Integer, db.ForeignKey('thesis.thesisid'), primary_key=True),
                        db.Column('isTrue', db.Boolean))

PersonItem = db.Table('person_item',
                      db.Column('personid', db.Integer, db.ForeignKey('person.personid'), primary_key=True),
                      db.Column('itemid', db.Integer, db.ForeignKey('item.itemid'), primary_key=True),
                      db.Column('isTrue', db.Boolean))

ThesisItem = db.Table('thesis_item',
                      db.Column('thesisid', db.Integer, db.ForeignKey('thesis.thesisid'), primary_key=True),
                      db.Column('itemid', db.Integer, db.ForeignKey('item.itemid'), primary_key=True),
                      db.Column('isTrue', db.Boolean))


class Person(db.Model):
    __tablename__ = "person"
    personid = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    lastname = db.Column(db.Text)
    firstname = db.Column(db.Text)
    birth = db.Column(db.Text)
    death = db.Column(db.Text)


class Thesis(db.Model):
    __tablename__ = "thesis"
    thesisid = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    provenance = db.Column(db.Text)
    decade = db.Column(db.Integer)
    defensedate = db.Column(db.Integer)
    isTrue = db.Column(db.Boolean)


class Item(db.Model):
    __tablename__ = "item"
    itemid = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    date = db.Column(db.Text)
    decade = db.Column(db.Integer)
    url = db.Column(db.Text)
    itemtype = db.Column(db.Text)


class Response(db.Model):
    __tablename__ = "response"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    thesisid = db.Column(db.Integer, db.ForeignKey('thesis.thesisid'))
    isTrue = db.Column(db.Boolean)
    answer = db.Column(db.Boolean)
    thesisProvenance = db.Column(db.Text)

    @staticmethod
    def add_response(these, answer):
        response = Response(thesisid=these.thesisid, isTrue=these.isTrue, answer=answer, thesisProvenance=these.provenance)
        try:
            db.session.add(response)
            db.session.commit()
            return response
        except Exception as e:
            return False, [str(e)]
