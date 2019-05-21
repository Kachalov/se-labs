# -*- coding: utf-8 -*-

import logging
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from app import config
from gevent import monkey

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


monkey.patch_all()
APP_MODE_CLI = 'cli'
APP_MODE_WEB = 'web'
APP_MODE_WORKER = 'worker'


def create_app(mode=None, **kwargs):
    logging.basicConfig(level=logging.DEBUG)

    app = Flask(__name__, **kwargs)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.config.from_object(config)
    app.config['MODE'] = APP_MODE_WEB if mode is None else mode

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    from app.extensions.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
