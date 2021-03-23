CREATE TABLE public.accounts
(
    id integer,
    name character varying NOT NULL,
    credit float NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO accounts (id, name, credit) VALUES (1,'First', 1000.00);

INSERT INTO accounts (id, name, credit) VALUES (2,'Second', 1000.00);

INSERT INTO accounts (id, name, credit) VALUES (3,'Third', 1000.00);

BEGIN TRANSACTION;
UPDATE accounts SET credit = 1000.00 WHERE name <> ' ';
SAVEPOINT first_point;
UPDATE accounts SET credit = credit - 500.00
    WHERE name = 'First';
UPDATE accounts SET credit = credit + 500.00
    WHERE name = 'Third';

SAVEPOINT second_point;
UPDATE accounts SET credit = credit - 700.00
    WHERE name = 'Second';
UPDATE accounts SET credit = credit + 700.00
    WHERE name = 'First';

SAVEPOINT third_point;
UPDATE accounts SET credit = credit - 100.00
    WHERE name = 'Second';
UPDATE accounts SET credit = credit + 100.00
    WHERE name = 'Third';
	
SAVEPOINT after_all_trans_point;


ROLLBACK to first_point;
ROLLBACK to second_point;
ROLLBACK to third_point;
ROLLBACK to after_all_trans_point;
COMMIT;
SELECT * FROM accounts;
