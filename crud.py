from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_restful import Resource, Api

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# api = Api(app)

# class UserInfo(Resource):
#     def get(self, id = -1, all = True, delete=False):
#         if delete == True and id != -1:
#             user_delete(id)
        
#         if id == -1:
#             return get_user()
#         else:
#             return user_detail(id)

#     def post(self):
#         add_user()

# api.add_resource(UserInfo, '/Nutrimi')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    address = db.Column(db.String(120))

    def __init__(self, username, email, address):
        self.username = username
        self.email = email
        self.address = address

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email', 'address')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    address = request.json['address']

    new_user = User(username, email, address)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)

# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']
    address = request.json['address']

    user.email = email
    user.username = username
    user.address = address

    db.session.commit()
    return user_schema.jsonify(user)

# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    fee = db.Column(db.Integer)
    dropoff_address = db.Column(db.String(200))
    pickup_address = db.Column(db.String(200))
    status = db.Column(db.Integer)

    def __init__(self, user_id, fee, dropoff_address, pickup_address, status):
        self.user_id = user_id
        self.fee = fee
        self.dropoff_address = dropoff_address
        self.pickup_address = pickup_address
        self.status = status

class TransactionSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('user_id', 'fee', 'dropoff_address', 'pickup_address', 'status')

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

# endpoint to create a new transaction
@app.route("/transaction", methods=["POST"])
def add_transaction():
    user_id = request.json['user_id']
    fee = request.json['fee']
    dropoff_address = request.json['dropoff_address']
    pickup_address = request.json['pickup_address']
    status = request.json['status']

    new_transaction = Transaction(user_id, fee, dropoff_address, pickup_address, status)

    db.session.add(new_transaction)
    db.session.commit()

    return jsonify(new_transaction)

# endpoint to get all transactions
@app.route("/transaction", methods=["GET"])
def get_transaction():
    all_transactions = Transaction.query.all()
    result = transactions_schema.dump(all_transactions)

    return jsonify(result.data)

# endpoint to get transaction detail by id
@app.route("/transaction/<id>", methods=["GET"])
def transaction_detail(id):
    transaction = Transaction.query.get(id)
    
    return transaction_schema.jsonify(transaction)

# endpoint to update transaction
@app.route("/transaction/<id>", methods=["PUT"])
def transaction_update(id):
    transaction = Transaction.query.get(id)
    user_id = request.json['user_id']
    fee = request.json['fee']
    dropoff_address = request.json['dropoff_address']
    pickup_address = request.json['pickup_address']
    status = request.json['status']

    transaction.user_id = user_id
    transaction.fee = fee
    transaction.dropoff_address = dropoff_address
    transaction.pickup_address = pickup_address
    transaction.status = status

    db.session.commit()

    return transaction_schema.jsonify(transaction)

# endpoint to delete transaction
@app.route("/user/<id>", methods=["DELETE"])
def transaction_delete(id):
    transaction = Transaction.query.get(id)
    db.session.delete(transaction)
    db.session.commit()

    return transaction_schema.jsonify(transaction)

if __name__=='__main__':
    app.run(debug=True)