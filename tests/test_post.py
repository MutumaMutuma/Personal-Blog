import unittest
from app.models import Post

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(id=56,title='My post',content='I can post all day long',category ='But wont',user_id= 15)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))