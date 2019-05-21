# -*- coding: utf-8 -*-

from nplusone.ext.flask_sqlalchemy import NPlusOne

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


nplusone = NPlusOne()


def init_app(app):
    nplusone.init_app(app)
