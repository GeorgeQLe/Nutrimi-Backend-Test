from flask import Flask

import os

from sqlite_flask import sqlite_flask

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')

app.register_blueprint(sqlite_flask)

if __name__=='__main__':
    app.run(debug=True)