import unittest
import os
import sys, json
from todo_app_sql_db import app

class apiTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.appli = app.test_client()

    def tearDown(self):
        pass

    def test_add(self):
        response = self.appli.post('/todo/api/v1.0/task/add',data = json.dumps(dict({'title':'hello', 'description' : 'world', 'done':'True'})), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_create_without_json(self):
        response = self.appli.post('/todo/api/v1.0/task/add')
        self.assertEqual(response.status_code, 400)


    def test_create_with_invalid_json(self):
        response = self.appli.post('/todo/api/v1.0/task/add',
                                 data=json.dumps(dict(status='changed')),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)






    def test_view(self):
        response = self.appli.get('/todo/api/v1.0/task/view', content_type='application/json')
        self.assertEqual(response.status_code, 200, "OK")

    def test_update(self):
        response = self.appli.put('/todo/api/v1.0/task/update/30',data=json.dumps(dict({'title':'Ali', 'description' : 'Ali'})), content_type = 'application/json')
        self.assertEqual(response.status_code, 200, "OK")

    def test_delete(self):
        response = self.appli.delete('/todo/api/v1.0/task/delete/30',data=json.dumps(dict({'title':'Ali', 'description' : 'Ali'})), content_type = 'application/json')
        self.assertEqual(response.status_code, 200, "OK")

if __name__ == "__main__":
    unittest.main()
