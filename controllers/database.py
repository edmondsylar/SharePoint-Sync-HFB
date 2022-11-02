# database class
# class has mainly two functions
# function one is to store the data passed to it in a tinydb database file named "synced_data.json"
# function two is to get the data from the tinydb database file named "synced_data.json"

import tinydb
from tinydb import TinyDB, Query

class Database:
    def __init__(self):
        self.db = TinyDB('synced_data.json')

    def storeData(self, data):
        self.db.insert(data)
        # retun the data stored in the database
        return self.db.all()

    def getData(self):
        return self.db.all()


# # Path: HFB\syncApi\controllers\sync.py
# # import the database class
# from database import Database

# # create an instance of the database class
# db = Database()

# # get the data from the database
# data = db.getData()

# # print the data
# print(data)