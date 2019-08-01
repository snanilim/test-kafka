import mysql.connector as mysql
from db_config import db_create_config

config = db_create_config()
connection = mysql.connect(**config)




cursor = connection.cursor()

# create db
cursor.execute("CREATE DATABASE logparse")


# show db
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print(databases)
for database in databases:
    print(database)
