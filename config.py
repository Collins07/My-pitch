SECRET_KEY = '\x0b\xeb"8\x85\xe9\xb1\x88M\xfcGOwEZS'

class Config:
    '''
    General configuration parent class
    '''



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