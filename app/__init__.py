from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

from app.models import init_db
from app.routes import init_routes
from app.utils.redis_util import init_redis
from config import get_config


def create_app() -> Flask:
    app = Flask(__name__)
    # 跨域配置
    CORS(app, supports_credentials=True)
    # 配置
    config = get_config()
    app.config.from_object(config)
    # 初始化数据表
    init_db(app, db)
    # 初始化redis
    init_redis(app)
    # 初始化路由
    init_routes(app)

    return app