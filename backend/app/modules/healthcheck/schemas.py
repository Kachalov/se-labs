# -*- coding: utf-8 -*-

from flask_restplus_patched import Schema
from flask_marshmallow import base_fields as fields

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


class HealthCheckSchema(Schema):
    name = fields.String(
        description='Name of service',
        dump_only=True,
    )

    version = fields.String(
        description='Version of service',
        dump_only=True,
    )

    build = fields.String(
        description='Build of service',
        dump_only=True,
    )

    db = fields.String(
        description='DB status',
        dump_only=True,
    )
