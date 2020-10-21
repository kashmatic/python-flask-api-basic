class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SECRET_KEY = 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://testuser:password@localhost:5432/vcpstatus'
    SQLALCHEMY_ECHO = True  ## to log errors

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
