import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# creating an engine object that takes care of communication between python and SQL
# engine = create_engine('postgresql://user:password@localhost:port/database')
engine = create_engine('postgresql://postgres@localhost:5432/postgres')
# or:
# engine = create_engine(os.getenv("DATABASE_URL")) # export DATABASE_URL = 'postgresql://user:password@localhost:port/database'

# making a session object for different users
db = scoped_session(sessionmaker(bind=engine))

def main():
	# db.execute returns a list of the queried rows
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
