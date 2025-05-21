from typing import Any
from flask import make_response


def Success(code: int = 200, msg: str = '', data: dict = None, sucess: str = 'true') -> dict[str, Any]:
    return make_response({
        'code': code,
        'msg': msg,
        'data': data,
        'success': sucess
    }, code)


def Fail(code: int = 400, msg: str = '', data: dict = None, success: str = 'false') -> dict[str, Any]:
    return make_response({
        'code': code,
        'msg': msg,
        'data': data,
        'success': success
    }, code)


def Error(code: int = 500, msg: str = '', data: dict = None, success: str = 'false') -> dict[str, Any]:
    return make_response({
        'code': code,
        'msg': msg,
        'data': data,
        'success': success
    }, code)


def Unauthorized(code: int = 401, msg: str = '', data: dict = None, success: str = 'false') -> dict[str, Any]:
    return make_response({
        'code': code,
        'msg': msg,
        'data': data,
        'success': success
    }, code)


def Forbidden(code: int = 403, msg: str = '', data: dict = None, success: str = 'false') -> dict[str, Any]:
    return make_response({
        'code': code,
        'msg': msg,
        'data': data,
        'success': success
    }, code)


