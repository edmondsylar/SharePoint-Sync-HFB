# using sqlite3 we are going to create a class to manage all database operations
# the main table structure is going to be as follows:
# [id, parent_site, child_site, status, timestamp]
# status will be either "Completed" or "Failed"

# import the necessary packages
import sqlite3
from sqlite3 import Error
import datetime
# import sleep to show output for some time period
from time import sleep

# import the dirsync
import dirsync
import os

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
        self.check_connection()
        # now create a table if it doesn't exist
        self.create_table()

    # check connection to the database
    def check_connection(self):
        if self.conn is not None:
            print("Connection to the database was successful")
            sleep(0.5)
        else:
            print("Connection to the database was not successful")
            sleep(0.5)

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
    def insert_record(self, parent_site, child_site):
        # create timestamp variable (date is today's date)
        date = datetime.datetime.now()
        status = "New"
        try:
            # sql query to insert 
            # parent_site, child_site, status, timestamp as the values
            sql = f"""INSERT INTO {self.table_name} (parent_site, child_site, status, timestamp)
                VALUES (?, ?, ?, ?)"""
            c = self.conn.cursor()
            # execute the query
            c.execute(sql, (parent_site, child_site, status, date))
            # commit the changes
            self.conn.commit()

            print("Record inserted successfully")
            return "Completed"

        except Error as e:
            print({
                "Message":"Failed to insert query",
                "Error": e
            })

from tinydb import TinyDB, Query
import datetime
from time import sleep

class tiny_connect:
    def __init__(self, client_name):
        self.client_name = client_name
        self.database_name = client_name + ".json"
        self.table_name = "Sharepoint_migrations"
        self.db = self.create_database()
        self.check_database()
        self.table = self.create_table()

    def check_database(self):
        if self.db:
            print("Database exists")
            sleep(0.5)
        else:
            print("Database does not exist")
            sleep(0.5)

    def create_database(self):
        try:
            db = TinyDB(self.database_name)
            return db
        except Error as e:
            print(e)
        return None

    def create_table(self):
        try:
            table = self.db.table(self.table_name)
            return table
        except Error as e:
            print(e)

    def insert_record(self, parent_site, child_site):
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = "New"
        try:
            record = {
                "parent_site": parent_site,
                "child_site": child_site,
                "status": status,
                "timestamp": date
            }
            self.table.insert(record)
            # after the insert is successful, call the sync_directories function
            return sync_directories(parent_site, child_site)            
            
        except Error as e:
            print({
                "Message":"Failed to insert query",
                "Error": e
            })

    # get all the records from the database
    def get_all_records(self):
        try:
            records = self.table.all()
            return records
        except Error as e:
            print({
                "Message":"Failed to get records",
                "Error": e
            })

    # ansync function to check if the record exists
    async def check_record(self, parent_site, child_site):
        try:
            record = Query()
            records = self.table.search((record.parent_site == parent_site) & (record.child_site == child_site))
            if records:
                # update the status of this recod to "Completed"
                self.table.update({"status":"Completed"}, (record.parent_site == parent_site) & (record.child_site == child_site))
                print({
                    "Message":"Record updated successfully",
                    "Record": records
                })
            else:
                return False
        except Error as e:
            print({
                "Message":"Failed to get records",
                "Error": e
            })

# function to sync the folders
def sync_directories(parent_dir, child_dir):
    sleep(2)
    try:
        # check if parent_dir and child_dir exist
        if not os.path.exists(parent_dir):
            print(f"{parent_dir} does not exist")
            return "Failed"
        if not os.path.exists(child_dir):
            print(f"{child_dir} does not exist")
            return "Failed"

        # synchronize directories
        dirsync.sync(parent_dir, child_dir, 'sync', purge=False)

        print(f"{parent_dir} synchronized to {child_dir}")
    except Exception as e:
        print(f"Failed to synchronize directories: {e}")
        return "Completed"

# 341711376
# New+1234
