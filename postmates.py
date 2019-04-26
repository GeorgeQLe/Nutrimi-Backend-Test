from flask import Blueprint, request
import requests
import json

from api_data import postmates_API_data, jsonify_postmates_API_data

customer_ID = "cus_MASWsf9DntbhIV"
signature_secret = "b0cda13d-fc65-4243-ae73-32c2a59b7612"
delivery_API_key_sandbox = "5f1b5928-69f7-49de-a2c9-b54fb68796d1"
postmates_url = "https://api.postmates.com/v1/customers/" + customer_ID + "/delivery_quotes"

postmates_api = Blueprint('postmates_api', __name__)

data = postmates_API_data()

@postmates_api.route("/delivery_to_address", methods=["POST"])
def add_delivery_address():
    data.user_address = request.json["delivery_to_address"]
    
    return jsonify_postmates_API_data(data)

@postmates_api.route("/delivery_from_address", methods=["POST"])
def add_restaurant_address():
    data.restaurant_address = request.json["delivery_from_address"]

    return jsonify_postmates_API_data(data)

@postmates_api.route("/both_addresses", methods=["POST"])
def add_both_addresses():
    data.user_address = request.json["delivery_to_address"]
    data.restaurant_address = request.json["delivery_from_address"]

    return jsonify_postmates_API_data(data)

@postmates_api.route("/get_addresses", methods=["GET"])
def get_addresses():
    return jsonify_postmates_API_data(data)

@postmates_api.route("/get_quote", methods=["GET"])
def get_quote():
    headers = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json',
        'Authorization' : 'Basic ' + delivery_API_key_sandbox
    }
    params = {
        "dropoff_address" : data.restaurant_address,
        "pickup_address" : data.user_address
    }

    r = requests.get(postmates_url, headers=headers, params=params)
    return json.dumps(r.json())