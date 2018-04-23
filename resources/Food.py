from flask import jsonify, request
from flask_restful import Resource
from model import db, redis_cache, FoodModel, RestaurantModel, FoodSchema
from Constants import FOOD_LIST
from ast import literal_eval
TAG = "Food"
foods_schema = FoodSchema(many=True)
food_schema = FoodSchema()


class FoodResource(Resource):
    def __init__(self):
        self.tag = "FoodResource"

    def get(self):
        if redis_cache.exists(FOOD_LIST):
            print("[%s.%s]Getting Food Data from redis Cache"%(TAG,self.tag))
            foods = redis_cache.__getitem__(FOOD_LIST)
            foods = literal_eval(foods.decode('utf8'))
        else:
            print("[%s.%s]Getting Food Data from sqlite db"%(TAG,self.tag))
            foods = FoodModel.query.all()
            foods = foods_schema.dump(foods).data
            redis_cache.__setitem__(FOOD_LIST,foods)

        return {"status":"success", "data":foods}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = food_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        restaurant_id = RestaurantModel.query.filter_by(id=data['restaurant_id']).first()
        if not restaurant_id:
            return {'status': 'error', 'message': 'food Restaurant not found'}, 400
        food = FoodModel(
            menu_id=json_data['menu_id'],
            restaurant_id=json_data['restaurant_id'],
            name=json_data['name'],
            description = json_data['description']
            )
        db.session.add(food)
        db.session.commit()

        result = food_schema.dump(food).data

        return {'status': "success", 'data': result}, 201


class FoodItemResource(Resource):

    def get(self, id):
        food = FoodModel.query.filter_by(id=id)
        food = foods_schema.dump(food).data
        return {'status': 'success', 'data': food}, 200

class RestaurantFoodResource(Resource):

    def get(self, id):
        food = FoodModel.query.filter_by(restaurant_id=id)
        food = foods_schema.dump(food).data
        return {'status': 'success', 'data': food}, 200

class RestaurantFoodItemResource(Resource):

    def get(self, id, foodId):
        food = FoodModel.query.filter_by(restaurant_id=id).filter_by(id=foodId)
        # foodItem = food.query.filye
        food = foods_schema.dump(food).data
        return {'status': 'success', 'data': food}, 200

class MenuFoodResource(Resource):

    def get(self, id):
        food = FoodModel.query.filter_by(menu_id=id)
        food = foods_schema.dump(food).data
        return {'status': 'success', 'data': food}, 200

class MenuFoodItemResource(Resource):

    def get(self, id, foodId):
        food = FoodModel.query.filter_by(menu_id=id).filter_by(id=foodId)
        food = foods_schema.dump(food).data
        return {'status': 'success', 'data': food}, 200
