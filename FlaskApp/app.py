# app.py 
# this file is going to be the main file for our application

# we are going to create a flask application and we are going to create the following routes
# 1. home
# 2. Sync_history
# 3. Search

# import the necessary packages
from flask import Flask, render_template, request, redirect, url_for
from Controller.main import Database

# import tiny_connect from Controller.
from Controller.main import tiny_connect

# create a flask application
app = Flask(__name__)

# create a database object
# create tiny connect object
db = tiny_connect("housing_finance")
client_intranet_name = "intranethf"

# create a home route
# route takes 2 methods GET and POST
# GET method is used to display the form
# POST method is used to process the form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # get the form data
        parent_site = request.form["parent_site"]
        # add the client intranet name to the parent site
        
        child_site = request.form["child_site"]

        insert = db.insert_record(parent_site, child_site)
        return redirect(url_for("home"))
    else:
        # get all the records in the database.
        all_records = db.get_all_records()
        # render the home page and pass the records to the home page
        return render_template("home.html", results=all_records)

# create a sync_history route
@app.route("/sync_history")
def sync_history():
    return render_template("sync_history.html")

# 

# search route
# this route has 2 methods GET and POST
# GET method is used to display the search form
# POST method is used to process the search form
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        # get the search term
        search_term = request.form["search_term"]
        # get the search results
        search_results = db.search_records(search_term)
        # render the search results
        return render_template("search_results.html", search_results=search_results)
    else:
        return render_template("search.html")
    
# run the application on port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)




