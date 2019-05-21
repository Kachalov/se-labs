# -*- coding: utf-8 -*-

from flask import current_app
from app.extensions.sqlalchemy import db

from flask_restplus_patched import Resource
from app.extensions.api import Namespace

from . import schemas

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'

api = Namespace('healthcheck', description='Health check')


@api.route('/')
class Healthcheck(Resource):
    @api.response(schemas.HealthCheckSchema())
    def get(self):
        app = current_app
        try:
            db.engine.execute('SELECT 1')
            db_health = 'OK'
        except Exception as e:
            db_health = str(e)

        return dict(
            name=app.config['NAME'],
            version=app.config['VERSION'],
            build=app.config['BUILD'],
            db=db_health,
        )
