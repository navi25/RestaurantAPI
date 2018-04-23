import os,sys
sys.path.append('../') #To allow lookup in parent directory too (Solving the python's infamous ModuleNotFound Exception :D)

import unittest
from urllib import response as rs, request as rq
from flask_testing import LiveServerTestCase
from run import create_app
import model
from model import db
import json


basedir = os.path.abspath(os.path.dirname(__file__))

class TestRestaurantCase(LiveServerTestCase):

    render_templates = False

    def create_app(self):
        self.app = create_app("config")
        self.client = self.app.test_client()
        return self.app

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_endPoint(self):
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/foods")
        self.assertEqual(response.code, 200)

    def test_content_type(self):
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/foods")
        self.assertEqual(response.headers["Content-Type"],"application/json")

    def test_empty_table(self):
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/foods")
        response_data = json.loads(response.read())
        self.assertEqual(len(response_data["data"]),0)

    def test_post_menu(self):
        data = dict(name="First Food", restaurant_id=1)
        response = self.client.post('/api/v1.0/foods',
                       data=json.dumps(data),
                       content_type='application/json')
        print(response.data)



if __name__ == '__main__':
    unittest.main()

