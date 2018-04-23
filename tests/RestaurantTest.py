import os,sys
sys.path.append('../') #To allow lookup in parent directory too (Solving the python's infamous ModuleNotFound Exception :D)

import unittest
from urllib import request as rq
from flask_testing import LiveServerTestCase
from run import create_app
from model import *
from config import PresentConfig
import json

basedir = os.path.abspath(os.path.dirname(__file__))

class TestRestaurantCase(LiveServerTestCase):

    render_templates = False

    def create_app(self):
        self.app = create_app(PresentConfig)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.init_app(self.app)
            redis_cache.init_app(self.app)
            db.create_all()
            db.session.commit()
        return self.app

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_endPoint(self):
        print("testing endpoint")
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/restaurants")
        self.assertEqual(response.code, 200)

    def test_content_type(self):
        print("testing content type")
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/restaurants")
        self.assertEqual(response.headers["Content-Type"],"application/json")

    def test_empty_table(self):
        print("testing empty table")
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/restaurants")
        response_data = json.loads(response.read())
        self.assertEqual(len(response_data["data"]),0)

    def test_post_restaurant(self):
        print("testing post restaurant")
        data = dict(name="First Test Restaurant")
        response = self.client.post('/api/v1.0/restaurants',
                       data=json.dumps(data),
                       content_type='application/json')
        print(json.loads(response.data))
        self.assertEqual(response.status_code, 201)

    def test_restaurant_data(self):
        print("testing restaurant data")
        data = dict(id=1,name="First Test Restaurant")
        self.client.post('/api/v1.0/restaurants',
                       data=json.dumps(data),
                       content_type='application/json')
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/restaurants")
        response_data = json.loads(response.read())
        print(response_data["data"][0])
        self.assertEqual(response_data["data"][0],data)

    def test_duplicate_restaurant(self):
        print("testing duplicate post restaurant")
        data = dict(name="First Test Restaurant")
        response1 = self.client.post('/api/v1.0/restaurants',
                       data=json.dumps(data),
                       content_type='application/json')

        response2 = self.client.post('/api/v1.0/restaurants',
                       data=json.dumps(data),
                       content_type='application/json')

        print(response1.data)
        print(response2.data)
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code,400)

    def test_delete_restaurant_caseExists(self):
        print("testing delete restaurant : CASE Rest EXISTS")
        data = dict(id=1,name="First Test Restaurant")
        response1 = self.client.post('/api/v1.0/restaurants',
                       data=json.dumps(data),
                       content_type='application/json')

        response2 = self.client.delete('/api/v1.0/restaurants',
                       data=json.dumps(data),
                       content_type='application/json')
        print(response1.data)
        print(response2.data)
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 204)



if __name__ == '__main__':
    unittest.main()

