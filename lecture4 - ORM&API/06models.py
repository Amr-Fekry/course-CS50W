from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)

# Object-Relational Mapping (ORM) allows us to use OOP syntax to interact with databases
# this is helpful as the SQL syntax become more complicated while the python ORM is relatively simpler

# sqlalchemy module allows us to execute explicit SQL statements through python code
# flask_sqlalchemy framework ties sqlalchemy module with a flask app to enable app users to more db features

# how to tie them?
# using flask_sqlalchemy framework we define a class for each table
# each class inherits "Model", a built-in relationship for interacting with the db
# for each class, set the __tablename__ and define columns of the table

# when we run db.create_all(), it translates the the classes into SQL's CREATE TABLE syntax

# finally, we can use the class objects to directly interact with the database without SQL commands


