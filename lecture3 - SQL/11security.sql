-- SQL INJECTION:
-- happens when we plug user input directly to the query

SELECT * FROM users 
	WHERE username = 'username' 
	AND password = 'password';

-- this query makes all accounts hackable through password =  1' OR '1' = '1
-- or it can update/delete/drop the database through the manipulation of the quotation marks in the input

-- SOLUTION: DB SANITIZATOIN: by escaping the special characters in user input before plugging it to the query

--------------------------------------------------

-- RACE CONDITIONS:
-- happens when a set of queries are accessed by different users at the same time (concurrently) and operations execute in a funky order

-- in an ATM withdrawal operation that consists of 2 query steps:
-- check if user have enough balance (SELECT), update balance (UPDATE), withdraw.
-- when two users have the same card and withdrawing $100 each concurrently from a balance of $100:
-- user1: 
SELECT balance FROM bank WHERE user_id = 1; -- returns 100
-- user2: 
SELECT balance FROM bank WHERE user_id = 1; -- returns 100
-- user1:
UPDATE bank SET balance = balance - 100 WHERE user_id = 1; -- balance = 0
-- user2:
UPDATE bank SET balance = balance - 100 WHERE user_id = 1; -- balance = -100

-- SOLUTION: TRANSACTIONS: which is locking the database while running a transaction (sequence of queries)

-- syntax of sql transactions

BEGIN;
-- SEQUENCE OF QUERIES HERE
COMMIT;

