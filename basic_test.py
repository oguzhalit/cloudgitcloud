from app import app as flask_app
import shutil, tempfile
from os import path
import unittest

def test_home_page():
    """
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_whoami():
    """
    WHEN the "/whoami" page is requested (POST)
    THEN check that the response is valid
    """
    with flask_app.test_client() as test_client:
        response = test_client.get('/whoami?firstname=oguz&lastname=sak')
        assert response.status_code == 200
        assert b'{"firstname":"oguz","lastname":"sak"}' in response.data

class test_usersFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        file = open('users.txt', 'w')
        file.seek(0)
        file.truncate()
        file.close()

    def test_something(self):
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        with open('users.txt', 'r') as fin: output = fin.readline().strip();
        f.write(f'{output}') 
        f = open(path.join(self.test_dir, 'test.txt'))
        self.assertEqual(f.read(), 'oguz:sak')

