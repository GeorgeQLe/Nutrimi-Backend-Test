from button import button_api
from flask_app import app
from sqlite import sqlite_flask
from yelp import yelp_api
from postmates import postmates_api

app.register_blueprint(button_api)
app.register_blueprint(postmates_api)
app.register_blueprint(sqlite_flask)
app.register_blueprint(yelp_api)

if __name__=='__main__':
    app.run(debug=True)
