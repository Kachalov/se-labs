# -*- coding: utf-8 -*-

from app.extensions.api import api

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


def init_app(app):
    if app.config['MODE'] == 'web':
        from . import schemas, resources
        api.add_namespace(resources.api)
