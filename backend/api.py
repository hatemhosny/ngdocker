#!usr/local/bin/python3

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from pymongo import MongoClient
import os



app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
client = MongoClient(os.environ['MONGODB_URL'],
    27017)
db = client.ahc
visits = db.visits

class Products(Resource):
    def get(self):
        return list(visits.find())


api.add_resource(Products, '/')

if __name__ == '__main__':
    app.run()
