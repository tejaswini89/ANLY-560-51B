#!/usr/bin/env python
# coding: utf-8

# In[8]:


import mysql.connector

connect = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1', database='sakila',
                              auth_plugin='mysql_native_password')
print(connect.connection_id)    

cursor = connect.cursor()

query = ("""select actor.first_name, actor.last_name, film_text.title, film_text.description 
from actor 
inner join film_actor on actor.actor_id = film_actor.actor_id
inner join film_text on film_actor.film_id = film_text.film_id
where title like 'zo%%'""")
                  
cursor.execute(query)

records = cursor.fetchall()

print("Total number of rows is: ", cursor.rowcount)

print("\nPrinting each record")

for row in records:
        print("first_name = ", row[0], )
        print("last_name = ", row[1])
        print("title = ", row[2])
        print("description  = ", row[3], "\n")
        
# disconnect from server
connect.close()

