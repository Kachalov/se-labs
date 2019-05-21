# -*- coding: utf-8 -*-

from flask_migrate import Migrate

from app.extensions.sqlalchemy import db

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


migrate = Migrate(db=db)


def init_app(app):
    migrate.init_app(app)
