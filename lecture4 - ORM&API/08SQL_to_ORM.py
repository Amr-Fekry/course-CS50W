
# creating a table

# CREATE TABLE flights (
#     id SERIAL PRIMARY KEY,
#     origin VARCHAR NOT NULL,
#     destination VARCHAR NOT NULL,
#     duration INTEGER NOT NULL
# );

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

db.create_all()

# ------------------------------------------

# inserting a row

# INSERT INTO flights 
# (origin, destination, duration) 
# VALUES 
# ('New York', 'Paris', 435);

# create a new flight object to insert
flight = Flight(origin="New York", destination="Paris", duration=435)

# add it to database
db.session.add(flight) # track command(s) 
db.session.commit() # execute all tracked commands in a transaction to prevent race-conditions

# ------------------------------------------

# selecting from table

# SELECT * FROM flights; 
Flight.query.all()

# SELECT * FROM flights WHERE origin = 'Paris'; 
Flight.query.filter_by(origin="Paris").all()

# SELECT * FROM flights WHERE origin = 'Paris' LIMIT 1; 
Flight.query.filter_by(origin="Paris").first()

# SELECT COUNT(*) FROM flights WHERE origin = 'Paris'; 
Flight.query.filter_by(origin="Paris").count()

# SELECT * FROM flights WHERE id = '28'; 
Flight.query.filter_by(id=28).first()
# or since it is common to query by id:
Flight.query.get(28)


# more advanced selecting: 

# SELECT * FROM flights ORDER BY origin; 
Flight.query.order_by(Flight.origin).all()

# SELECT * FROM flights ORDER BY origin DESC; 
Flight.query.order_by(Flight.origin.desc()).all()

# SELECT * FROM flights WHERE origin != 'Paris'; 
Flight.query.filter(Flight.origin != "Paris").all()
# filter_by takes a parameter of the search key
# filter takes a boolean expression

# SELECT * FROM flights WHERE origin LIKE '%a%'; 
Flight.query.filter(Flight.origin.like("%a%")).all()

# SELECT * FROM flights WHERE origin IN ('Tokyo','Paris'); 
Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()

# SELECT * FROM flights WHERE origin = 'Paris' AND duration > 500; 
Flight.query.filter(and_(Flight.origin == "Paris", Flight.duration > 500)).all()
# SELECT * FROM flights WHERE origin = 'Paris' OR duration > 500; 
Flight.query.filter(or_(Flight.origin == "Paris", Flight.duration > 500)).all()
# and_ , or_ need to be imported from sqlalchemy

# SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id;
db.session.query(Flight, Passenger).filter(Flight.id == Passengers.flight_id).all()


# using relationships:

# SELECT * FROM passengers WHERE flight_id = 1;
Passenger.query.filter_by(flight_id=1).all()
# or using a defined relationship (airline4/models.py)
Flight.query.get(1).passengers

# SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE passenger.name = "Alice";
p = Passenger.query.filter_by(name="Alice")
Flight.query.get(p.flight_id)
# or using a defined relationship (airline4/models.py)
Passenger.query.filter_by(name="Alice").first().flight


# None is returned if no matches where found

# ------------------------------------------

# updating a row

# UPDATE flights SET duration = 280 WHERE id = 6;

flight = Flight.query.get(6)
flight.duration = 280

# then we need to commit the changes

# ------------------------------------------

# deleting a row

# DELETE FROM flights WHERE id = 28;

flight = Flight.query.get(28)
db.session.delete(flight)

# ------------------------------------------

# COMMIT;
db.session.commit()


