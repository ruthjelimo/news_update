class Config:
    '''
    General configuration parent class
    '''
             
    BASE_URL='https://newsapi.org/v2/top-headlines/sources?language=en&category={}&apiKey={}'
    # ARTICLE_URL ='https://newsapi.org/v2/sources?language=en&headlines={}&apiKey={}'
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