# Dependencies and Setup
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

# Flask Setup
app = Flask(__name__)

# PyMongo Connection Setup
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    destination_data = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    # Run the scrape function
    mars_data = scrape_mars.scrape_all()

    # Update the Mongo database using update and upsert=True
    mars.update_one({}, {"$set": mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/", code = 302)


if __name__ == "__main__":
    app.run(debug=True)
