# Copyright 2019 George Le

from flask import Blueprint, request
import requests

from api_data import yelp_API_data, jsonify_yelp_API_data

yelp_API_key = "oToW9DcEi0MK8_v2h-zy_ix6Rn12aPKCvKMGdItF1hfKu9qUtQwwTWppZfAHAwEOULuS9PMoescrdNFlaor_U6xCFErbqSbO3EgNqsZxoe71w7akib-Oj3SJzA-sXHYx"

yelp_api = Blueprint('yelp_api', __name__)

data = yelp_API_data()

@yelp_api.route("/setup_food_and_address", methods=["POST"])
def change_food_and_address():
    data.food_type = request.json["food_type"]
    data.location = request.json["location"]

    return jsonify_yelp_API_data(data) 

@yelp_api.route("/setup_limit", methods=["POST"])
def change_limit():
    data.limit = request.json["limit"]

    return jsonify_yelp_API_data(data)

@yelp_api.route("/setup_open_now", methods=["POST"])
def change_open_now():
    data.limit = request.json["open_now"]

    return jsonify_yelp_API_data(data)

@yelp_api.route("/setup_sort_by", methods=["POST"])
def change_sort_by():
    data.limit = request.json["sort_by"]

    return jsonify_yelp_API_data(data)

@yelp_api.route("/setup_all", methods=["POST"])
def change_all():
    data.food_type = request.json["food_type"]
    data.location = request.json["location"]
    data.limit = request.json["limit"]
    data.limit = request.json["open_now"]
    data.limit = request.json["sort_by"]

    return jsonify_yelp_API_data(data)

yelp_url = 'https://api.yelp.com/v3/businesses/search'

@yelp_api.route("/yelp_call", methods=["GET"])
def search_businesses():
    headers = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + yelp_API_key
    }
    params = {
        "term": data.food_type,
        "location": data.location,
        "limit": data.limit,
        "open_now": data.open_now,
        "sort_by": data.sort_by
    }

    r = requests.get(yelp_url, headers=headers, params= params)
    return r