import os

class Config:
    '''
    general configuration
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SPECIFI_API_URL
    
class ProdConfig(Config):
    '''
    production configuration
    '''
    pass
class DevConfig(Config):
    '''
    development configuration
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}

