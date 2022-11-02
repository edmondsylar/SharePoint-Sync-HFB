#signature - ptyped.
# create a flastrestful api with 3 endpoints
# end point 1: /api/v1.0/SyncData
# end point 2: /api/v1.0/GetSyncedData
# end point 3: /api/v1.0/Homepage
# the end point 1 is used to sync data from parent folder to child folder

# parent folder location is: D:\\Development\\HFB\\tests\\parentdir
#child folder location is: D:\\Development\\HFB\\tests\\childir

# the end point 2 is used to get the synced data from the child folder and display it on the browser.
# end point 3 is used to display the homepage of the api wih the a link to the end point 1 and end point 2 and a message "Welcome to the HFB Sync API".

import os
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from dirsync import sync

# import the database class from controllers/database.py
from controllers.database import Database

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# endpoint 1: /api/v1.0/SyncData


@app.route('/')
def index():
    return render_template('index.html')

# end point 1: /api/v1.0/SyncData
# function takes 2 arguments from the request body
@app.route('/api/v1.0/SyncData', methods=['POST'])
def syncData():
    parent_folder = request.form.get('parent_folder')
    child_folder = request.form.get('child_folder')
    # command to sync the directories.
    sync(parent_folder, child_folder, 'sync', purge=True)
    # create an instance of the database class
    db = Database()
    # get the number of records in the database
    data_ = db.getData()
    # get the length of the data
    length = len(data_)
    
    # create a dictionary to store the data
    data = {
        "id": length+1,
        'parent_folder': parent_folder,
        'child_folder': child_folder
    }
    # store the data in the database
    db.storeData(data)

    # return redirect to the homepage with a message `Data synced successfully`
    return render_template('index.html', message="Data synced successfully")
    

# end point 2: /api/v1.0/GetSyncedData.
# function takes 1 argument from the request body
# function to get the synced data from the child folder and display it on the browser.

@app.route('/api/v1.0/GetSyncedData', methods=['POST'])
def getSyncedData():
    child_folder = request.form.get('child_folder')
    # command to get the synced data from the child folder.
    synced_data = os.listdir(child_folder)
    return jsonify({'synced_data': synced_data})



# new endpoint to return the db-view page from the templates folder
# function returns the db-view page with the data from the database named `data`
@app.route('/api/v1.0/DbView')
def dbView():
    db = Database()
    data = db.getData()
    return render_template('db-view.html', data=data)

# run the api.
if __name__ == '__main__':
    app.run(debug=True, port=5100)