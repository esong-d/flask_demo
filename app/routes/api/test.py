from flask import Blueprint, current_app, json


from app.utils.resp_format import Success, Fail


test_bp = Blueprint('test', __name__)


@test_bp.route('/t')
def test_route():
    data = dict(current_app.config)
    data.pop('PERMANENT_SESSION_LIFETIME')
    return Success(msg="test success", data=data)