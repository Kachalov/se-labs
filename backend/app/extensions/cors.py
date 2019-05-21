# -*- coding: utf-8 -*-

from flask_cors import CORS

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


cors = CORS(
    resources={'/*': {'origins': '*'}},
    supports_credentials=True,
)


def init_app(app):
    cors.init_app(app)
