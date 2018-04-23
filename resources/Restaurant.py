from flask import request
from flask_restful import Resource
from model import db, redis_cache, RestaurantModel, RestaurantSchema
from Constants import RESTAURANT_LIST
import json
restaurants_schema = RestaurantSchema(many=True)
restaurant_schema = RestaurantSchema()
from ast import literal_eval

TAG = "Restaurant"

class RestaurantResource(Resource):
    def __init__(self):
        self.tag = "RestaurantResource"

    def get(self):
        if redis_cache.exists(RESTAURANT_LIST):
            print("[%s.%s]Getting Restaurant Data from redis Cache"%(TAG,self.tag))
            restaurants = redis_cache.__getitem__(RESTAURANT_LIST)
            restaurants = literal_eval(restaurants.decode('utf8'))
        else:
            print("[%s.%s]Getting Restaurant Data from sqlite db"%(TAG,self.tag))
            restaurants = RestaurantModel.query.all()
            restaurants = restaurants_schema.dump(restaurants).data
            redis_cache.__setitem__(RESTAURANT_LIST,restaurants)

        return {'status': 'success', 'data': restaurants}, 200


    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = restaurant_schema.load(json_data)
        if errors:
            return errors, 422
        restaurant = RestaurantModel.query.filter_by(name=data['name']).first()
        if restaurant:
            return {'message': 'Restaurant already exists'}, 400
        restaurant = RestaurantModel(
            name=json_data['name']
            )

        db.session.add(restaurant)
        db.session.commit()

        result = restaurant_schema.dump(restaurant).data

        return { "status": 'success', 'data': result }, 201


    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = restaurant_schema.load(json_data)
        if errors:
            return errors, 422
        restaurant = RestaurantModel.query.filter_by(id=data['id']).first()
        if not restaurant:
            return {'message': 'Restaurant do not exist'}, 400
        restaurant.name = data['name']
        db.session.commit()

        result = restaurant_schema.dump(restaurant).data

        return { "status": 'success', 'data': result }, 204


    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = restaurant_schema.load(json_data)
        if errors:
            return errors, 422
        restaurant = RestaurantModel.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = restaurant_schema.dump(restaurant).data

        return { "status": 'success', 'data': result}, 204


class RestaurantItemResource(Resource):

    def get(self, id):
        restaurant = RestaurantModel.query.filter_by(id=id)
        restaurant = restaurants_schema.dump(restaurant).data
        return {'status': 'success', 'data': restaurant}, 200


