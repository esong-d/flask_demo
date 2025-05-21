from flask import Blueprint


from .auth import auth_bp



def init_admin_bps():
    admin_bp = Blueprint('admin', __name__)
    
    # 注册子蓝图
    admin_bp.register_blueprint(auth_bp, url_prefix='/auth')

    return admin_bp