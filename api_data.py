# Copyright 2019 George Le

from flask import jsonify

class Postmates_data():
    def __init__(self, restaurant_address = " ", user_address = " "):
        self.restaurant_address = restaurant_address
        self.user_address = user_address

def jsonify_postmates_API_data(data= Postmates_data()):
    return jsonify(data.restaurant_address,
                    data.user_address)

class yelp_API_data:
    def __init__(self, food_type = " ", location = " ", limit=10, open_now = True, sort_by = "rating"):
        self.food_type = food_type
        self.location = location
        self.limit = limit
        self.open_now = open_now
        self.sort_by = sort_by

def jsonify_yelp_API_data(data = yelp_API_data()):
    return jsonify(food_type = data.food_type,
                    location = data.location,
                    limit = data.limit,
                    open_now = data.open_now,
                    sort_by = data.sort_by)