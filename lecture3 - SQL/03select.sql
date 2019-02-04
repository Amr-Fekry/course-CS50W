-- reading from a database

-- read columns from a table for all rows:
-- SELECT (columns) FROM (table);
SELECT * FROM flights;
SELECT origin, destination FROM flights;

-- read columns from a table for specific row(s):
-- SELECT (columns) FROM (table) WHERE (booleans);
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;

-- SELECT (columns) FROM (table) WHERE (range);
SELECT * FROM flights WHERE origin IN ('New York', 'Lima');
-- which is equivalent to
SELECT * FROM flights WHERE origin = 'New York' OR origin = 'Lima';

-- string matching 
SELECT * FROM flights WHERE origin LIKE '%a%';
-- where % is a placeholder for 0 or more characters
-- result is all rows with origin containing an 'a'

-- apply a function on (columns)
SELECT COUNT(*) FROM flights;
SELECT AVG(duration) FROM flights;
SELECT COUNT(*) FROM flights WHERE origin = 'New York';
SELECT AVG(duration) FROM flights WHERE origin = 'New York';
-- SUM(), MIN(), MAX()