import mysql.connector as mysql

def db_create_config():
    db = {
        "host": "localhost",
        "user": "root",
        "passwd": "admin@123"
    }
    return db


def db_base_config():
    db = {
        "host": "localhost",
        "user": "root",
        "passwd": "admin@123",
        "database": "logparse"
    }
    return db