from flask_app import app
from sqlite import sqlite_flask
from yelp import yelp_api

app.register_blueprint(sqlite_flask)
app.register_blueprint(yelp_api)

if __name__=='__main__':
    app.run(debug=True)