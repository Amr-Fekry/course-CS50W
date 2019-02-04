import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine('postgresql://user:password@localhost:port/database')
engine = create_engine('postgresql://postgres@localhost:5432/postgres')
# engine = create_engine(os.getenv("DATABASE_URL"))

db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("""INSERT INTO flights (origin, destination, duration) 
                      VALUES (:origin, :destination, :duration)""",
                      {"origin": origin, "destination": destination, "duration": duration})
        
        # sqlalchemy takes care of SQL INJECTIONS
        # placeholders like :name are substituted with variables from the dict following the query
        # and these are automatically sanetize the variables by escaping special characters
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()

    # sqlalchemy takes care of RACE CONDITIONS 
    # treats a starting query as a transaction, so we need to "commit" at the end of every sequence of queries 
    # db.execute() tracks queries
    # db.commit() starts executing the tracked queries


if __name__ == "__main__":
    main()
