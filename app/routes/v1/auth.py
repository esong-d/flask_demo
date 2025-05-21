from flask import Flask, request, current_app, Blueprint

from app.utils.resp_format import Success, Fail


auth_bp = Blueprint('auth', __name__)


@auth_bp.route(rule='/code', methods=['GET'])
def get_code():
    return Success(msg='获取验证码成功')


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    return Success(msg='注册成功')


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    return Success(msg='登录成功')