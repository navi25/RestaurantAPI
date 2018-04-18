from flask import Blueprint
from flask_restful import Api
from resources.Restaurant import RestaurantResource, RestaurantItemResource
from resources.Food import FoodResource, RestaurantFoodResource, RestaurantFoodItemResource

api_bp = Blueprint('api/v1.0', __name__)
api = Api(api_bp)

# Route
api.add_resource(RestaurantResource, '/restaurants')
api.add_resource(RestaurantItemResource, '/restaurants/', '/restaurants/<int:id>', endpoint='id')
api.add_resource(RestaurantFoodResource, '/restaurants/<int:id>/foods')
api.add_resource(RestaurantFoodItemResource, '/restaurants/<int:id>/foods/<int:foodId>')
api.add_resource(FoodResource,'/foods')



