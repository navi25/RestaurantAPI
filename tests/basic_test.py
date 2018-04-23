import os,sys
sys.path.append('../') #To allow lookup in parent directory too (Solving the python's infamous ModuleNotFound Exception :D)

import unittest
from urllib import response as rs, request as rq
from flask_testing import LiveServerTestCase
from run import create_app
from model import db
from config import TestingConfig

basedir = os.path.abspath(os.path.dirname(__file__))

class TestBaseCase(LiveServerTestCase):

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

    def test_base_food_endPoint(self):
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/foods")
        self.assertEqual(response.code, 200)

    def test_base_restaurant_endPoint(self):
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/restaurants")
        self.assertEqual(response.code, 200)

    def test_base_menu_endPoint(self):
        response = rq.urlopen(self.get_server_url() + "/api/v1.0/menus")
        self.assertEqual(response.code, 200)



if __name__ == '__main__':
    unittest.main()

