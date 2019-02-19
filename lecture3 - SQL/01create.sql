-- first, a database must be created, then it can contain multiple tables.

-- creating (designing) a table

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);


-- CREATE TABLE table-name (
--     column1-name data-type properties,
--     column2-name data-type properties,
--     column3-name data-type properties,
--     column4-name data-type properties,
-- );

-- data-types: 
-- INTEGER 
-- DECIMAL
-- SERIAL (auto incrementing integer, starting from 1)
-- VARCHAR
-- TIMESTAMP
-- BOOLEAN
-- ENUM (one of a set of integers)

-- properties & constraints:
-- PRIMARY KEY (unique value to refernce the row)
-- NOT NULL (must have a value in each row)
-- UNIQUE (unique value for each row)
-- DEFAULT (set a default value if not given)
-- CHECK (only allow a value in a specific range)


-- altering a table after creating it
ALTER TABLE table-name ADD CONSTRAINT constraint_name UNIQUE (column1-name, column2-name,..);
-- or:
ALTER TABLE table-name ADD UNIQUE (column1-name, column2-name,..);


-- clear a table (removes all data, id counter continues)
TRUNCATE TABLE table-name

-- 	delete a table
DROP TABLE table-name





