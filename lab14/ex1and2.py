import redis
import time
import json
r = redis.Redis(
host='redis-13261.c253.us-central1-1.gce.cloud.redislabs.com',
port="13261",
password='eEpPhXYpT9dCz56aFba3ElPrnqYeWcIK')

# To clear the database
# r.flushdb()

customers = []
customers.append(
    {"customer_numb": '001', "first_name": 'Jane', "last_name": 'Doe'}
)
customers.append(
    {"customer_numb": '002', "first_name": 'John', "last_name": 'Doe'}
)
customers.append(
    {"customer_numb": '003', "first_name": 'Jane', "last_name": 'Smith'}
)
customers.append(
    {"customer_numb": '004', "first_name": 'John', "last_name": 'Smith'}
)
customers.append(
    {"customer_numb": '005', "first_name": 'Jane', "last_name": 'Jones'}
)
customers.append(
    {"customer_numb": '006', "first_name": 'John', "last_name": 'Jones'}
)

# To add all customers from the array
# for i in range(len(customers)):
#     r.hset('Customers','c' + str(i), json.dumps(customers[i]))

orders = []
orders.append(
    {"order_numb": '1001', "customer_numb": '002', "order_date": '10/10/09', "order_total": '250.85'}
)
orders.append(
    {"order_numb": '1002', "customer_numb": '002', "order_date": '2/21/10', "order_total": '125.89'}
)
orders.append(
    {"order_numb": '1003', "customer_numb": '003', "order_date": '11/15/09', "order_total": '1567.99'}
)
orders.append(
    {"order_numb": '1004', "customer_numb": '004', "order_date": '11/22/09', "order_total": '180.92'}
)
orders.append(
    {"order_numb": '1005', "customer_numb": '004', "order_date": '12/15/09', "order_total": '565.00'}
)
orders.append(
    {"order_numb": '1006', "customer_numb": '006', "order_date": '11/22/09', "order_total": '25.00'}
)
orders.append(
    {"order_numb": '1007', "customer_numb": '006', "order_date": '10/8/09', "order_total": '85.00'}
)
orders.append(
    {"order_numb": '1008', "customer_numb": '006', "order_date": '12/29/09', "order_total": '109.12'}
)

# To add all orders from the array
# for i in range(len(orders)):
#     r.hset('Orders','o' + str(i), json.dumps(orders[i]))

profile = []
profile.append(
    {"login": 'e.petrashko@innopolis.university', "id": 0, "Followers": [], "Following": [], "Posts": []}
)
profile.append(
    {"login": 'a.burmyakov@university', "id": 1, "Followers": [], "Following": [], "Posts": []}
)

profile[0]['Followers'].append(1)
profile[1]['Followers'].append(0)
profile[0]['Following'].append(1)
profile[1]['Following'].append(0)

posts = []

posts.append(
    {"post_id" : 0,"user_id": 0, "time": time.time()}
)

posts.append(
    {"post_id" : 1, "user_id": 1, "time": time.time()}
)

profile[0]['Posts'].append(0)
profile[1]['Posts'].append(1)

# To add all the profiles from the profile array
# for i in range(len(profile)):
#     r.hset('Profiles','pr' + str(i), json.dumps(profile[i]))

# To add all the posts from the post array
# for i in range(len(posts)):
#     r.hset('Posts','po' + str(i), json.dumps(posts[i]))

# Display all entries
print('Customers')
for i in range(len(customers)):
    print(r.hget('Customers', 'c' + str(i)))

print('Orders')
for i in range(len(orders)):
    print(r.hget('Orders', 'o' + str(i)))

print('Profiles')
for i in range(len(profile)):
    print(r.hget('Profiles', 'pr' + str(i)))

print('Posts')
for i in range(len(posts)):
    print(r.hget('Posts', 'po' + str(i)))







