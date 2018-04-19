from flask import Blueprint
from flask_restful import Api
from resources.Restaurant import RestaurantResource, RestaurantItemResource
from resources.Food import FoodResource, RestaurantFoodResource, RestaurantFoodItemResource, MenuFoodResource, MenuFoodItemResource
from resources.Menu import MenuResource, MenuItemResource

api_bp = Blueprint('api/v1.0', __name__)
api = Api(api_bp)

# Route For Restaurants endpoints
api.add_resource(RestaurantResource, '/restaurants')
api.add_resource(RestaurantItemResource, '/restaurants/<int:id>')
api.add_resource(RestaurantFoodResource, '/restaurants/<int:id>/foods')
api.add_resource(RestaurantFoodItemResource, '/restaurants/<int:id>/foods/<int:foodId>')

# Route for Menu endpoint
api.add_resource(MenuResource,'/menus')
api.add_resource(MenuItemResource,'/menus/<int:id>')
api.add_resource(MenuFoodResource, '/menus/<int:id>/foods')
api.add_resource(MenuFoodItemResource, '/menus/<int:id>/foods/<int:foodId>')

# Route For Food endpoint
api.add_resource(FoodResource,'/foods')



