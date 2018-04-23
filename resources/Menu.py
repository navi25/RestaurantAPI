from flask import jsonify, request
from flask_restful import Resource
from model import db, redis_cache, MenuModel, RestaurantModel, MenuSchema
from Constants import MENU_LIST
menus_schema = MenuSchema(many=True)
menu_schema = MenuSchema()
from ast import literal_eval

TAG = "Menu"

class MenuResource(Resource):
    def __init__(self):
        self.tag = "MenuResource"

    def get(self):
        if redis_cache.exists(MENU_LIST):
            print("[%s.%s]Getting Menu Data from redis Cache"%(TAG,self.tag))
            menus = redis_cache.__getitem__(MENU_LIST)
            menus = literal_eval(menus.decode('utf8'))
        else:
            print("[%s.%s]Getting Menu Data from sqlite db"%(TAG,self.tag))
            menus = MenuModel.query.all()
            menus = menus_schema.dump(menus).data
            redis_cache.__setitem__(MENU_LIST,menus)

        return {"status":"success", "data":menus}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = menu_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        restaurant_id = RestaurantModel.query.filter_by(id=data['restaurant_id']).first()
        if not restaurant_id:
            return {'status': 'error', 'message': 'Menu Restaurant not found'}, 400
        menu = MenuModel(
            restaurant_id=json_data['restaurant_id'],
            name=json_data['name']
            )
        db.session.add(menu)
        db.session.commit()

        result = menu_schema.dump(menu).data

        return {'status': "success", 'data': result}, 201

class MenuItemResource(Resource):

    def get(self, id):
        menu = MenuModel.query.filter_by(id=id)
        memu = menus_schema.dump(menu).data
        return {'status': 'success', 'data': menu}, 200
