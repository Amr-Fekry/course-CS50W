-- SQL allows nesting queries and combining them into one

-- return the flights with more than one passenger
SELECT * FROM flights WHERE id IN 
(SELECT flight_id FROM passengers GROUP BY flight_id 
HAVING COUNT(*) > 1);

-- parenthesis are executed first then the result is used to complete the parent query.
