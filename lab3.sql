--1)
SELECT * FROM country WHERE country_id >= 12 AND country_id <= 17 ORDER BY country_id ASC;
--2)
SELECT * FROM address WHERE city_id IN(SELECT city_id FROM city WHERE city LIKE 'A%');
--3)
SELECT first_name, last_name, city FROM customer INNER JOIN address ON customer.address_id = address.address_id
INNER JOIN city ON city.city_id = address.city_id;
--4)
SELECT * FROM customer WHERE customer_id IN (SELECT customer_id FROM payment WHERE amount > 11);
--5)
SELECT first_name, COUNT(first_name)
FROM customer
GROUP BY first_name
HAVING COUNT(first_name)>1

--2nd task
--1)
CREATE VIEW person_test AS
SELECT first_name, last_name, email
FROM customer
WHERE active >= 1;

--2)
CREATE VIEW person_staff AS
SELECT first_name, last_name, email, password
FROM staff
WHERE active = true;

CREATE OR REPLACE FUNCTION public.person_set_password()
	RETURNS TRIGGER
	LANGUAGE PLPGSQL
	AS
$$
BEGIN
	NEW.password = '111';
	RETURN NEW;
END;
$$

CREATE TRIGGER person_set_def_pass
BEFORE INSERT
ON public.staff
FOR EACH ROW
EXECUTE PROCEDURE person_set_password();

