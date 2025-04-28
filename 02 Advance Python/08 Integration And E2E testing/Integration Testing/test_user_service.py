import unittest
from user_service import UserService
from database import Database

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.user_service = UserService(self.database)
    
    def test_create_user(self):
        result = self.user_service.create_user('Radhika')
        assert result == 'User with the name Radhika created!!!'

    def test_create_existing_user(self):
        self.user_service.create_user('Radhika')
        result = self.user_service.create_user('Radhika')
        assert result == 'User with the name Radhika is exist'

# This test ensures that UserService interacts correctly with the Database. 