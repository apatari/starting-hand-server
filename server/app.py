#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource
from range_helpers import update_range, get_range

# Local imports
from config import app, db, api
# Add your model imports


# Views go here!

# @app.route('/')
# def index():
#     return '<h1>Project Server</h1>'

class Range(Resource):

    def get(self):
        ranges = get_range()

        return ranges, 200
    
    def post(self):
        hand = request.get_json()['hand']
        update_range(hand)
        return get_range(), 201
    

api.add_resource(Range, '/api/ranges')


if __name__ == '__main__':
    app.run(port=5000, debug=True)

