import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(id=56,title='My pitch',content='I can pitch all day long',category ='But wont',user_id= 15)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

