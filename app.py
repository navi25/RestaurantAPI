from flask import Blueprint
from flask_restful import Api
from resources.Restaurant import RestaurantResource
from resources.Food import FoodResource

api_bp = Blueprint('api/v1.0', __name__)
api = Api(api_bp)

# Route
api.add_resource(RestaurantResource, '/restaurants')
api.add_resource(FoodResource,'/foods')
