# -*- coding: utf-8 -*-

import os
from distutils.util import strtobool
from werkzeug.security import gen_salt

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


conf = os.environ.get

CURRENT_CONFIG_VERSION = '1'
CONFIG_VERSION = conf('CONFIG_VERSION', '1')

if CONFIG_VERSION != CURRENT_CONFIG_VERSION:
    raise TypeError('Configuration out of date: required %s, but got %s' % (
        CURRENT_CONFIG_VERSION,
        CONFIG_VERSION,
    ))

JSON_AS_ASCII = False
RESTPLUS_JSON = dict(ensure_ascii=JSON_AS_ASCII)
DEBUG = strtobool(conf('DEBUG', 'false'))
TESTING = strtobool(conf('TESTING', 'false'))
PROPAGATE_EXCEPTIONS = True
SCHEME = 'https' if strtobool(conf('HTTPS', 'true')) else 'http'

SECRET_KEY = conf('SECRET_KEY', gen_salt(128))

SQLALCHEMY_DATABASE_URI = conf('DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SOCKETIO_QUEUE = conf('SOCKETIO_QUEUE', None)

REDIS_URL = conf('REDIS_URL', None)

try:
    JWT_ALGORITHM = 'RS256'
    with open('jwt.key', 'r') as key:
        JWT_PRIVATE_KEY = key.read()
    with open('jwt.pub', 'r') as pub:
        JWT_PUBLIC_KEY = pub.read()
except:
    JWT_ALGORITHM = 'HS256'
JWT_ALGORITHM = conf('JWT_ALGORITHM', JWT_ALGORITHM)
JWT_SECRET_KEY = SECRET_KEY
JWT_USER_CLAIMS = 'claims'
JWT_IDENTITY_CLAIM = 'sub'

JWT_TOKEN_LOCATION = ['headers', 'cookies']
JWT_SESSION_COOKIE = False
JWT_COOKIE_CSRF_PROTECT = True

AUTHORIZATIONS = []

VERSION = conf('SERVICE_VERSION')
NAME = conf('SERVICE_NAME')
PUBLIC_NAME = conf('SERVICE_PUBLIC_NAME')
BUILD = conf('SERVICE_BUILD')
TITLE = 'SE Labs'
DESCRIPTION = ''

APP_EXTENSIONS = None
APP_MODULES = None
