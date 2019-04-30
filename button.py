from flask import Blueprint, request
from random import randint

import requests

button_api = Blueprint('button_api', __name__)

class Button_info:
    choice = 0
    def __init__(self):
        pass

@button_api.route("/button", methods=["POST"])
def button_api():
    Button_info.choice = randint(0, 10) 
    return Button_info.choice

@button_api.route("/button_choice", methods=["GET"])
def get_button_choice():
    return Button_info.choice
