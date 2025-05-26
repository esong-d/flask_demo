from flask import json
from flask import Response


class BaseResponse(Response):
    default_mimetype = 'application/json'

    def __init__(self, code: int, success: bool, msg: str, data: dict = None):
        _dict = {
            'code': code,
            'success': success,
            'msg': msg,
            'data': data
        }
        super().__init__(json.dumps(_dict), status=code)


class Success(BaseResponse):
    def __init__(self, code: int = 200, msg: str = '', data: dict = None, success: str = 'true') -> None:
        super().__init__(code=code, msg=msg, data=data, success=success)


class Fail(BaseResponse):
    def __init__(self, code: int = 400, msg: str = '', data: dict = None, success: str = 'false') -> None:
        super().__init__(code=code, msg=msg, data=data, success=success)


class Error(BaseResponse):
    def __init__(self, code: int = 500, msg: str = '', data: dict = None, success: str = 'false') -> None:
        super().__init__(code=code, msg=msg, data=data, success=success)


class Unauthorized(BaseResponse):
    def __init__(self, code: int = 401, msg: str = '', data: dict = None, success: str = 'false') -> None:
        super().__init__(code=code, msg=msg, data=data, success=success)


class Forbidden(BaseResponse):
    def __init__(self, code: int = 403, msg: str = '', data: dict = None, success: str = 'false') -> None:
        super().__init__(code=code, msg=msg, data=data, success=success)



