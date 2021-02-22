import psycopg2
from faker import Faker
import random
# https://stackabuse.com/working-with-postgresql-in-python/

con = psycopg2.connect(database="postgres", user="postgres",
                       password="postgres", host="localhost", port="5432")

print("Database opened successfully")

cur = con.cursor()
# TABLE CREATION
# cur.execute('''CREATE TABLE CUSTOMER
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       ADDRESS        TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       REVIEW         TEXT    NOT NULL);''')
# print("Table created successfully")

# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')")
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')")
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')")
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')")
# cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
# cur.execute("DELETE from STUDENT where ADMISSION=3420;")
# con.commit()
# print("Record inserted successfully")
# cur = con.cursor()
# cur.execute("SELECT admission, name, age, course, department from STUDENT")
# rows = cur.fetchall()

# print(rows)
# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[3])
#     print("DEPARTMENT =", row[4], "\n")
# print("Operation done successfully")
# con.close()

# DATA CREATION

# fake = Faker()
# for i in range(100000):
#     cur.execute(
#         "INSERT INTO CUSTOMER (ID,NAME,ADDRESS,AGE,REVIEW) VALUES ( " + str(i) + ",'" + fake.name() + "', '" + fake.address() +"', " + str(random.randint(15, 85)) + ", '" + fake.text() +"')")
# con.commit()


# cur.execute("EXPLAIN ANALYZE SELECT name, address FROM CUSTOMER WHERE name = 'Evgeny'")
# rows = cur.fetchall()
# print(rows)

# First Table

# [('Seq Scan on customer  (cost=0.00..4337.00 rows=2 width=58) (actual time=17.242..17.242 rows=0 loops=1)',), ("  Filter: (name = 'Evgeny'::text)",), ('  Rows Removed by Filter: 100000',), ('Planning Time: 1.104 ms',), ('Execution Time: 17.278 ms',)]

# With hash
# [('Bitmap Heap Scan on customer  (cost=4.02..11.89 rows=2 width=58) (actual time=0.029..0.029 rows=0 loops=1)',), ("  Recheck Cond: (name = 'Evgeny'::text)",), ('  ->  Bitmap Index Scan on first_hash_index  (cost=0.00..4.01 rows=2 width=0) (actual time=0.028..0.028 rows=0 loops=1)',), ("        Index Cond: (name = 'Evgeny'::text)",), ('Planning Time: 1.500 ms',), ('Execution Time: 0.081 ms',)]


# TABLE CREATION

# cur.execute('''CREATE TABLE CUSTOMER2
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       ADDRESS        TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       REVIEW         TEXT    NOT NULL);''')
# print("Table created successfully")

# DATA CREATION

# fake = Faker()
# for i in range(100000):
#     cur.execute(
#         "INSERT INTO CUSTOMER2 (ID,NAME,ADDRESS,AGE,REVIEW) VALUES ( " + str(i) + ",'" + fake.name() + "', '" + fake.address() +"', " + str(random.randint(15, 85)) + ", '" + fake.text() +"')")
# con.commit()

cur.execute("EXPLAIN ANALYZE SELECT name, address FROM CUSTOMER2 WHERE age = 20")
rows = cur.fetchall()
print(rows)

# Second Table

# [('Seq Scan on customer2  (cost=0.00..4342.00 rows=1500 width=58) (actual time=0.075..17.910 rows=1483 loops=1)',), ('  Filter: (age = 20)',), ('  Rows Removed by Filter: 98517',), ('Planning Time: 1.171 ms',), ('Execution Time: 17.990 ms',)]

# With btree

# [('Bitmap Heap Scan on customer2  (cost=19.92..2605.49 rows=1500 width=58) (actual time=0.319..4.312 rows=1483 loops=1)',), ('  Recheck Cond: (age = 20)',), ('  Heap Blocks: exact=1196',), ('  ->  Bitmap Index Scan on second_btree_index  (cost=0.00..19.54 rows=1500 width=0) (actual time=0.209..0.209 rows=1483 loops=1)',), ('        Index Cond: (age = 20)',), ('Planning Time: 1.462 ms',), ('Execution Time: 4.411 ms',)]


con.close()
