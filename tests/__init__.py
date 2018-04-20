import os
import tempfile
import unittest
import sys

sys.path.append('../') #To allow lookup in parent directory too (Solving the python's infamous ModuleNotFound Exception :D)

from run import app as flaskApp

testApp = flaskApp.test_client()

class TestApp(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskApp.config['DATABASE'] = tempfile.mkstemp()
        flaskApp.testing = True
        with flaskApp.app_context():
            flaskApp.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskApp.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()

