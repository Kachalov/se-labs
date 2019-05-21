# -*- coding: utf-8 -*-

from flask_marshmallow import Marshmallow
from json import JSONEncoder
from uuid import UUID

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


marshmallow = Marshmallow()


def init_app(app):
    marshmallow.init_app(app)

    JSONEncoderDefault = JSONEncoder.default

    def JSONEncoderNew(self, o):
        if isinstance(o, UUID):
            return str(o)
        return JSONEncoderDefault(self, o)

    JSONEncoder.default = JSONEncoderNew
