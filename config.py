# class Config:
#     '''
#     General configuration parent class
#     '''
             
#     BASE_URL='https://newsapi.org/v2/top-headlines/sources?language=en&category={}&apiKey={}'
#     # ARTICLE_URL ='https://newsapi.org/v2/sources?language=en&headlines={}&apiKey={}'
# class ProdConfig(Config):
#     '''
#     Production  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     pass
    

# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     DEBUG = True

import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    NEWS_SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    # NEWS_TOP_HEADLINE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    CAT_API_URL='https://newsapi.org/v2/top-headlines?category={}&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY= os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}