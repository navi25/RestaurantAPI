import os,sys
sys.path.append('../') #To allow lookup in parent directory too (Solving the python's infamous ModuleNotFound Exception :D)

import unittest

from run import app as flask_app
from flask_sqlalchemy import SQLAlchemy
from model import db
from urllib import response as rs, request as rq
from flask import Flask
from flask_testing import LiveServerTestCase
from run import create_app
from model import db
basedir = os.path.abspath(os.path.dirname(__file__))

class TestBaseCase(LiveServerTestCase):

    render_templates = False

    def create_app(self):
        self.app = create_app("config")
        return self.app

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
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

