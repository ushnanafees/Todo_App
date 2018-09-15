import unittest
import os
import sys, json
import  todo_app_sql_db

class apiTest(unittest.TestCase):
    def setUp(self):
        todo_app_sql_db.config['TESTING'] = True
        self.app = todo_app_sql_db.test_client()
        todo_app_sql_db.config['DEBUG'] = False


    def tearDown(self):
        pass

    def test_add(self):
        response = self.app.post('/todo/api/v1.0/task/add',data=json.dumps(dict({'title':'First', 'description' : 'Lase'})), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # def test_update(self):
    #    response = self.todo_app_sql_db.put('/todo/api/v1.0/task/update/18')
    #    self.assertEqual(response.status_code, 200 OK)

if __name__ == "__main__":
    unittest.main()
