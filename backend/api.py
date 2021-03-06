#!usr/local/bin/python3

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


class Products(Resource):
    def get(self):
        return {
            'products': ['Ice cream',
                         'Chocolate',
                         'fruits',
                         'juice'
                         ]
        }


api.add_resource(Products, '/')

if __name__ == '__main__':
    app.run()
