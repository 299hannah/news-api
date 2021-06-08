import unittest
from app.models import News_source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method thatt will run before every Test
        '''
        self.new_source = News_source('news_id', 'name')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_source))