# using sqlite3 we are going to create a class to manage all database operations
# the main table structure is going to be as follows:
# [id, parent_site, child_site, status, timestamp]
# status will be either "Completed" or "Failed"

# import the necessary packages
import sqlite3
from sqlite3 import Error

# create a class to manage all database operations
# the class will have the following methods:
# 1. insert a new record
# 2. Check all records
# 3. Check given record
# 4. The database connection is initialized in the constructor
# 4. The class takes one argument which is a client_name.

class Database:
    def __init__(self, client_name):
        self.client_name = client_name
        self.database_name = client_name + ".db"
        self.table_name = "Sharepoint_migrations"
        self.conn = self.create_connection()
        self.create_table()

    # create a connection to the database
    def create_connection(self):
        try:
            conn = sqlite3.connect(self.database_name)
            return conn
        except Error as e:
            print(e)
        return None

    # create a table in the database
    def create_table(self):
        try:
            sql = f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                id integer PRIMARY KEY,
                parent_site text NOT NULL,
                child_site text NOT NULL,
                status text NOT NULL,
                timestamp text NOT NULL
            );"""
            c = self.conn.cursor()
            c.execute(sql)
        except Error as e:
            print(e)

    # insert a new record into the database
    def insert_record(self, parent_site, child_site, status, timestamp):
        try:
            sql = f"""INSERT INTO {self.table_name} (parent_site, child_site, status, timestamp)
                VALUES (?, ?, ?, ?)"""
            c = self.conn.cursor()
            c.execute(sql, (parent_site, child_site, status, timestamp))
            self.conn.commit()
        except Error as e:
            print(e)

    # check all records in the database
    def check_all_records(self):
        try:
            sql = f"""SELECT * FROM {self.table_name}"""
            c = self.conn.cursor()
            c.execute(sql)
            return c.fetchall()
        except Error as e:
            print(e)

    # check a specific record in the database
    def check_record(self, record_id):
        try:
            sql = f"""SELECT * FROM {self.table_name} WHERE id=?"""
            c = self.conn.cursor()
            c.execute(sql, (record_id,))
            return c.fetchall()
        except Error as e:
            print(e)