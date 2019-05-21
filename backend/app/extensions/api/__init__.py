# -*- coding: utf-8 -*-
"""
Commit: https://github.com/frol/flask-restplus-server-example/commit/
        328d4ad033ade338091cce8c1667ea7098a14567
"""

from copy import deepcopy
from flask import Blueprint

from .api import Api
from .namespace import Namespace
from .http_exceptions import abort


api = Api()
bp = Blueprint('api', __name__)


def init_app(app):
    path = '/{app[PUBLIC_NAME]}/{app[VERSION]}'.format(app=app.config)
    bp.url_prefix = path
    api.init_app(
        bp,
        title=app.config.get('TITLE', app.config['NAME']),
        version=app.config['VERSION'],
        description=app.config.get('DESCRIPTION'),
        doc=None,
        base_path=path,
    )
    api.authorizations = deepcopy(app.config['AUTHORIZATIONS'])

    # app.register_blueprint(bp)
