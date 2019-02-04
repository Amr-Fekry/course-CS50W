-- indexing values of a column makes it quicker to reference them later
-- it is used for the frequently referenced columns

CREATE INDEX duration_index ON flights (duration);

-- indexing speeds up referencing, but shouldn't be used on many columns
-- because it needs to be updated with each table update, which might make the overall process slower

-- a trade off to be mindfull of
