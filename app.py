from types import new_class
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from bs4 import BeautifulSoup
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
mars_db_collection = mongo.db.scraped_information

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    scraped_data_from_db = mars_db_collection.find_one()
    scraped_headline = scraped_data_from_db['news']['headline'][0]
    return render_template("index.html", scraped_info=scraped_data_from_db,scraped_headline = scraped_headline)


@app.route("/scrape")
def scraper():
    freshly_scraped_data = scrape_mars.scrape()
    mars_db_collection.update({}, freshly_scraped_data, upsert = True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
