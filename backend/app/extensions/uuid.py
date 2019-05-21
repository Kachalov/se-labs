# -*- coding: utf-8 -*-

from flask_uuid import FlaskUUID

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


uuid = FlaskUUID()


def init_app(app):
    uuid.init_app(app)
