import unittest
from models import User, Post

class TestUser(unittest.TestCase):


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"    










if __name__ == '__main__':
        unittest.main()        

