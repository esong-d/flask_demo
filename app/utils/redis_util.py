from flask_redis import FlaskRedis


redis0 = FlaskRedis(config_prefix="REDIS0")
redis1 = FlaskRedis(config_prefix="REDIS1")


def init_redis(app):
    redis0.init_app(app)
    redis1.init_app(app)