from flask import Flask
import sys
from data import tasks

# Bad Idea - no globals
# using this variable in place of database
global_list = tasks

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

