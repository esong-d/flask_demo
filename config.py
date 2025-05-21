import os

from regex import F



class BaseConfig(object):
    SECRET_KEY = '123456'
    JWT_SECRET_KEY = '123456'

    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,  # 确保连接健康
        'pool_recycle': 3600,   # 连接池中的连接在60分钟不活动后将被回收
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:abc123456@localhost:3306/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS0_URL = "redis://@127.0.0.1:6379/0" 
    REDIS1_URL = "redis://@127.0.0.1:6379/1"


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/foodie'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


def get_config(env: str = None):
    if not env:
        env = os.environ.get('FLASK_ENV', 'development')
        return configs.get(env)
    return configs.get(env)
