# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion
from sqlalchemy_utils import force_instant_defaults

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


force_auto_coercion()
force_instant_defaults()
db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
