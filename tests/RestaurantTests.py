#This tests the Restaurant End points
import nose
from nose.tools import *
# from tests import testApp
import json
import sys

sys.path.append('../') #To allow lookup in parent directory too (Solving the python's infamous ModuleNotFound Exception :D)


from run import app as flaskApp

testApp = flaskApp.test_client()

def check_content_type(headers):
  eq_(headers['Content-Type'], 'application/json')

def get_json_response(data):
  if data is None:
    return ""
  return json.loads(data.decode(sys.getdefaultencoding()))


def test_restaurant_routes():
  rv = testApp.get('/restaurants/')
  check_content_type(rv.headers)
  resp = get_json_response(rv.data)

  #make sure we get a response
  eq_(rv.status_code,200)

  #make sure there are no restaurants
  eq_(len(resp), 0)

  #create a restaurant
  d = dict(name="first restaurant")
  rv = testApp.post('/restaurants/', data=d)
  check_content_type(rv.headers)
  eq_(rv.status_code,201)

  #Verify we sent the right data back
  resp = get_json_response(rv.data)
  eq_(resp["name"],"first restaurant")

  #Get restaurants again...should have one
  rv = testApp.get('/restaurants/')
  check_content_type(rv.headers)
  resp = get_json_response(rv.data)
  #make sure we get a response
  eq_(rv.status_code,200)
  eq_(len(resp), 1)

  #GET the restaurant with specified ID
  rv = testApp.get('/users/%s' % resp[0]['id'])
  check_content_type(rv.headers)
  eq_(rv.status_code,200)
  resp = get_json_response(rv.data)
  eq_(resp["name"],"first restaurant")

  #Try and add Duplicate User Email
  rv = testApp.post('/restaurants/', data=d)
  check_content_type(rv.headers)
  eq_(rv.status_code,500)

if __name__ == '__main__':
    test_restaurant_routes()
