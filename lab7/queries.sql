-- QUERY 1
SELECT cus.first_name, cus.last_name, f.title FROM customer cus, film f, category cat, film_category fc 
WHERE (f.rating = 'R' or f.rating = 'PG-13') AND (f.film_id = fc.film_id and fc.category_id = cat.category_id) AND (cat.name = 'Horror' or cat.name = 'Sci-Fi') AND f.title
NOT IN (select f2.title FROM rental r, inventory i, film f2 WHERE 
		(cus.customer_id = r.customer_id AND r.inventory_id = i.inventory_id AND i.film_id = f2.film_id));
		 
		 
EXPLAIN ANALYZE SELECT cus.first_name, cus.last_name, f.title FROM customer cus, film f, category cat, film_category fc 
WHERE (f.rating = 'R' or f.rating = 'PG-13') AND (f.film_id = fc.film_id and fc.category_id = cat.category_id) AND (cat.name = 'Horror' or cat.name = 'Sci-Fi') AND f.title
NOT IN (select f2.title FROM rental r, inventory i, film f2 WHERE 
		(cus.customer_id = r.customer_id AND r.inventory_id = i.inventory_id AND i.film_id = f2.film_id));
-- It's too slow query, so we can improve it by adding some indexes to the tables for example for 'raiting' and 'category_id'
--QUERY 2

SELECT st.store_id, SUM(pay.amount)
FROM store st
	INNER JOIN staff sf ON st.store_id = sf.store_id
	INNER JOIN payment pay ON pay.staff_id = sf.staff_id
		WHERE pay.payment_date >= (SELECT MAX(payment_date) FROM payment) - INTERVAL '1 month' 
GROUP BY st.store_id;

EXPLAIN ANALYZE SELECT st.store_id, SUM(pay.amount)
FROM store st
	INNER JOIN staff sf ON st.store_id = sf.store_id
	INNER JOIN payment pay ON pay.staff_id = sf.staff_id
		WHERE pay.payment_date >= (SELECT MAX(payment_date) FROM payment) - INTERVAL '1 month' 
GROUP BY st.store_id;
-- Expensive part is when we select by date.
--We can improve by creating (btree)index of payment_date


