import unittest
from app.models import News_Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = News_Article('title', 'description', 'url', 'image', 'published_on')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,News_Article))