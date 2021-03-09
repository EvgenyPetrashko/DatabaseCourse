CREATE OR REPLACE FUNCTION retrievecustomers(start_id integer, end_id integer)
RETURNS TABLE
(
    customer_id integer,
    store_id smallint,
    first_name character varying(45),
    last_name character varying(45),
    email character varying(50),
    address_id smallint,
    activebool boolean,
    create_date date,
    last_update timestamp without time zone,
    active integer
)
LANGUAGE plpgsql
AS 
$$
BEGIN
	IF end_id < 0 OR end_id >= 600 OR end_id < start_id OR start_id < 0 OR start_id >= 600 THEN
		RAISE EXCEPTION 'Incorrect parrameters';
	END IF;
	
	RETURN QUERY
	SELECT * FROM customer cus
	WHERE cus.address_id >= start_id AND cus.address_id <= end_id
	ORDER BY cus.address_id;
END;
$$