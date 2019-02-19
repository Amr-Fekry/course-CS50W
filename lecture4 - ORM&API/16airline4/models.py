import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    # feature3: define a relationship property to connect the two tables
    passengers = db.relationship("Passenger", backref="flight", lazy=True)
    # relationship is between Flight and Passenger tables
    # Flight objects can use this property to extract Passenger objects related
    # (think of "passengers" as a keyword to reference Passenger objects from a related Flight object)
    # backref: the keyword to reference a Filght object from a related Passenger object
    # lazy evaluate: don't fetch the info of this property in Flight objects until it is actually used

    # feature2: take advantage of methods and give objects of table classes the ability to execute a set of instructions 
    def add_passenger(self, name):
        p = Passenger(name=name, flight_id=self.id)
        db.session.add(p)
        db.session.commit()


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
