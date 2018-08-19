from flask import Flask, jsonify, request
import sys
from data import tasks
from modelFurniture import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def get_tasks():
    return jsonify({'Error': 'inside index case'})

@app.route("/furniture", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_furniture():
    if(request.method == 'GET'):
        return router(request.method, 'Furniture')
    elif(request.method == 'POST'):
        return router(request.method, 'Furniture')
    elif(request.method == 'PUT'):
        return router(request.method, 'Furniture')
    elif(request.method == 'DELETE'):
        return router(request.method, 'Furniture')
    else:
       return jsonify({'Error': 'could not determine HTTP verb'})

@app.route("/cart", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_cart():
    if(request.method == 'GET'):
        return router(request.method, 'Cart')
    elif(request.method == 'POST'):
        return router(request.method, 'Cart')
    elif(request.method == 'PUT'):
        return router(request.method, 'Cart')
    elif(request.method == 'DELETE'):
        return router(request.method, 'Cart')
    else:
       return jsonify({'Error': 'could not determine HTTP verb'})

def router(method, model):
    if(method == 'GET'):
        return eval('_get' + model + '()')
    if(method == 'POST'):
        return eval('_create' + model + '()')
    if(method == 'PUT'):
        return eval('_update' + model + '()')
    if(method == 'DELETE'):
        return eval('_delete' + model + '()')

def _getFurniture():
    sort_by_location = request.args.get('sortBy')
    sort_by_availability = request.args.get('sortBy')
    sort_by_life_left = request.args.get('sortBy')
    location_name = request.args.get('location_name')

    if location_name is not None:
        return jsonify(getFurnitureHelper(location_name))
    if sort_by_location is not None:
        return jsonify(getFurnitureSortedByLocation())
    elif sort_by_availability is not None:
        getFurnitureSortedByAvailability()
    elif sort_by_life_left is not None:
        getFurnitureSortedByLifeLeft()
    else:
        return jsonify({'furniture': tasks})

def _createFurniture():
    return jsonify({'furniture': 'create new furniture'})

def _updateFurniture():
    return jsonify({'furniture': 'update existing furniture'})

def _deleteFurniture():
    return jsonify({'furniture': 'delete furniture'})

def _getCart():
    if not request.json or not 'user_id' in request.json:
        return jsonify({'cart': carts})
    else:
        user_id = request.json.get('user_id')
        return jsonify(getCart(user_id))

def _createCart():
    if not request.json or not 'user_id' in request.json:
        return jsonify({'Error' : 'provide user id'})
    else:
        user_id = request.json.get('user_id')
        print(user_id)
        return jsonify(addToCart(user_id))

def _updateCart():
    return jsonify({'cart': 'reached update cart'})

def _deleteCart():
    return jsonify({'furniture': 'reached delete cart'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)

