import mysql.connector as mysql
from db_config import db_base_config

config = db_base_config()
connection = mysql.connect(**config)


cursor = connection.cursor()

# create table
cursor.execute("CREATE TABLE logs (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, date VARCHAR(255), src_mac VARCHAR(255), src_ip VARCHAR(255), src_port VARCHAR(255), dst_ip VARCHAR(255), dst_port VARCHAR(255), net VARCHAR(255))")
# cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")


# drop table
# cursor.execute("DROP TABLE logs")


# show table info
cursor.execute("DESC logs")
print(cursor.fetchall())


# [('Jul 22 10:54:38', '6e:24:74:00:39:1d', '103.78.248.25', '3306', '198.20.103.242', '3306'), ('Jul 22 10:54:38', 'ac:d1:b8:eb:d8:ff', '192.168.3.126', '55049', '74.125.130.100', '55049'), ('Jul 22 10:54:38', '00:0c:42:f3:c9:e4', '103.78.248.34', '55049', '74.125.130.100', '55049'), ('Jul 22 10:54:38', '60:a4:4c:af:8a:c9', '192.168.2.128', '59994', '157.240.190.209', '59994'), ('Jul 22 10:54:39', 'cc:2d:e0:e4:53:92', '103.78.248.90', '54656', '45.255.127.163', '54656'), ('Jul 22 10:55:05', 'b8:69:f4:9f:49:a0', '103.78.248.98', '51361', '145.226.46.148', '51361'), ('Jul 22 11:02:43', 'b8:81:98:43:9e:ff', '192.168.3.144', '50366', '103.78.248.70', '50366'), ('Jul 22 11:02:43', '6c:3b:6b:90:22:3c', '103.78.248.70', '1723', '103.78.248.34', '1723')]

