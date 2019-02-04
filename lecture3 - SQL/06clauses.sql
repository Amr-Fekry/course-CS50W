-- reading a specific number of rows
SELECT * FROM flights LIMIT 2;

-- reading rows ordered ascendingly/descendingly
SELECT * FROM flights ORDER BY duration ASC;
SELECT * FROM flights ORDER BY duration DESC;

SELECT * FROM flights ORDER BY duration ASC LIMIT 3;

-- reading a specific column displaying no of repetitoins 
SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

-- HAAVING is similar to WHERE clause, except it follows GROUP BY
