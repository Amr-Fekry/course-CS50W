-- SQL is a Relational DBMS because it can connect (relate) tables together 
-- "foreign keys" are a method used to connect tables

-- as the app grows, one table can get complicated,
-- and data gets repeated (redundancy)

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    origin_code VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    destination_code VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

-- a better design is to separate each type of entity in a table:
-- (flights, locations, passengers) and relate these tables togehter

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin_id INTEGER REFERENCES locations,
    destination_id INTEGER REFERENCES locations,
    duration INTEGER NOT NULL
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    code VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
);

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

-- foreign keys are named (name_id) by convention, 
-- a foreign key indicates referencing an id (PRIMARY KEY) from another table

-- relating tables usinf foreign keys saves storage space and helps keep things organized

-- REFERENCES keyword inforces a foreign key constraint on the references table 
-- so that id column (primary key) can't be changed as long as the table is referenced.



