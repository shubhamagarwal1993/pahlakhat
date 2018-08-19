from flask import Flask
import sys
from data import tasks

# Bad Idea - no globals
# using this variable in place of database
global_list = tasks
carts = {}

def getFurnitureHelper(location_name):
    furniture_list = []
    for obj in global_list:
        if (obj["Category"] == "Furniture"):
            furniture_list.append(obj["Product Name"])
    return {location_name: furniture_list}

def getFurnitureSortedByLocation():
    del global_list[:]
    return {'test': global_list}

def getFurnitureSortedByAvailability():
    return {'Error': 'inside availability sorted furniture'}

def getFurnitureSortedByLifeLeft():
    return {'Error': 'inside life left sorted furniture'}

def getCart(user_id):
    if user_id in carts :
        user_cart = carts[user_id]
    else :
        user_cart = []
    return {'cart': user_cart}

def addToCart(user_id):
    default_furniture = {
        "Category": "Furniture",
        "Sub-Category": "Bed Frame",
        "Budget Sub-Category": "Bed Frame",
        "Product Name": "Modway upholstered platform bed  w/headboard",
        "Product Description": "I am a new furniture",
        "Brand": "",
        "Current Unit Cost": "",
        "Warehoused Quantity (DNE)": 2,
        "68 West Willetta": "",
        "1102 West Turney": "",
        "1301 W. 14th Street #14": 1,
        "1301 W. 14th Street #15": "",
        "639 N. 5th Avenue": "",
        "4142 25th Street #21": "",
        "846 N. 2nd Avenue #2A": "",
        "1128 Grand Avenue unit #B201": ""
    }

    if user_id in carts :
        user_cart = carts[user_id]
        user_cart.append(default_furniture)
    else :
        user_cart = []
        user_cart.append(default_furniture)
    carts[user_id] = user_cart
    return {'status': 'added to your cart'}
