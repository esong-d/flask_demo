from flask import Flask

from .admin import init_admin_bps
from .v1 import init_v1_bps
from .api import init_api_bps


__all__ = ["init_routes"]


def init_routes(app: Flask):
    # 注册总路由
    app.register_blueprint(init_admin_bps(), url_prefix="/admin")
    app.register_blueprint(init_v1_bps(), url_prefix="/app/v1")
    app.register_blueprint(init_api_bps(), url_prefix="/api")