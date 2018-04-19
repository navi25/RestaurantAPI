from flask import jsonify, request
from flask_restful import Resource
from model import db, FoodModel, RestaurantModel, FoodSchema

foods_schema = FoodSchema(many=True)
food_schema = FoodSchema()

class FoodResource(Resource):
    def get(self):
        foods = FoodModel.query.all()
        foods = foods_schema.dump(foods).data
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
