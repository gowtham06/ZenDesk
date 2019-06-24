import unittest
from MongoConnect import *
from command_line_app import command_line
import sys
from os import listdir
from os.path import isfile, join

class TestMongoConnection(unittest.TestCase):
    def test_connection(self):
        mongoConnect=MongoConnection("localhost",27017,"zendesk")
        # self.assertEquals(mongoConnect.check_connection(),"True") 
        with self.subTest():
            self.assertIsNotNone(mongoConnect.check_connection())
        with self.subTest():
            self.assertEqual(mongoConnect.check_connection(),True)
    
    def test_close_connection(self):
        mongoConnect=MongoConnection("localhost",27017,"zendesk")

        with self.subTest():
            self.assertIsNone(mongoConnect.close_connection())
    def test_command_line_app(self):
        files = [join('TestsInput',f) for f in listdir('TestsInput') if isfile(join('TestsInput', f))]
        for file in files:
            stdin = sys.stdin
            with open(file,'r') as fileRead:
                sys.stdin = fileRead
                with self.subTest():
                    self.assertIsNotNone(command_line())
    def test_null_parameter(self):
        mongoConnect=MongoConnection("localhost",27017,"zendesk")
        with self.subTest():
            self.assertGreaterEqual(len(mongoConnect.execute_query('organizations','details',"null")),1)
        mongoConnect.close_connection()

    def test_multiple_value_parameter(self):
        mongoConnect=MongoConnection("localhost",27017,"zendesk")
        with self.subTest():
            self.assertGreaterEqual(len(mongoConnect.execute_query('tickets','tags',"California")),1)
        mongoConnect.close_connection()
    
    def test_boolean_value(self):
        mongoConnect=MongoConnection("localhost",27017,"zendesk")
        with self.subTest():
            self.assertGreaterEqual(len(mongoConnect.execute_query('users','active',"true")),1)
        mongoConnect.close_connection()
    
    def test_empty_value_parameter(self):
        mongoConnect=MongoConnection("localhost",27017,"zendesk")
        with self.subTest():
            self.assertIsNotNone(mongoConnect.execute_query('tickets','description',""))
        mongoConnect.close_connection()
        

if __name__ == "__main__":
    unittest.main()