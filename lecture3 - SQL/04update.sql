-- changing data in a table

-- UPDATE (table) SET (column = new-value) WHERE (row restrictions)
UPDATE flights SET duration = 430 WHERE origin = 'New York' AND destination = 'London';
UPDATE flights SET duration = duration + 15 WHERE origin = 'New York' AND destination = 'London';

-- updates cannot be undone, but database backups can be made 
