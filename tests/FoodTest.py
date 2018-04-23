import os,sys
sys.path.append('../') #To allow lookup in parent directory too (Solving the python's infamous ModuleNotFound Exception :D)

import unittest
from urllib import response as rs, request as rq
from flask_testing import LiveServerTestCase
from run import create_app
import model
from model import db
import json
from config import TestingConfig

basedir = os.path.abspath(os.path.dirname(__file__))

class TestFoodCase(LiveServerTestCase):

    render_templates = False

    def create_app(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()
            db.session.commit()
        return self.app

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_endPoint(self):
        print("testing food endpoint")
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/foods")
        self.assertEqual(response.code, 200)

    def test_content_type(self):
        print("testing food content type")
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/foods")
        self.assertEqual(response.headers["Content-Type"],"application/json")

    def test_empty_table(self):
        print("testing food empty table")
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/foods")
        response_data = json.loads(response.read())
        self.assertEqual(len(response_data["data"]),0)

    def test_post_food(self):
        print("testing food post")
        data = dict(name="First Food", restaurant_id=1, menu_id =1, description="Tasty Food from South India")
        dataM = dict(name="First Menu", restaurant_id=1)
        dataR = dict(name="First Test Restaurant")
        self.client.post('/api/v1.0/restaurants',
                       data=json.dumps(dataR),
                       content_type='application/json')
        self.client.post('/api/v1.0/menus',
                       data=json.dumps(dataM),
                       content_type='application/json')
        response = self.client.post('/api/v1.0/foods',
                       data=json.dumps(data),
                       content_type='application/json')
        print(response.data)



if __name__ == '__main__':
    unittest.main()

