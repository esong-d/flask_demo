from flask import Flask, Blueprint

from .test import test_bp


def init_api_bps():
    api_bp = Blueprint('api_bp', __name__)

    api_bp.register_blueprint(test_bp, url_prefix='/test')

    return api_bp