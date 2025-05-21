from flask import Blueprint

from .auth import auth_bp


def init_v1_bps():
    v1_bp = Blueprint('v1', __name__)

    # 注册子蓝图
    v1_bp.register_blueprint(auth_bp, url_prefix='/auth')

    return v1_bp