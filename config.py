import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('6592b1e01d031f6fee363c2d6f8e14bd')



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