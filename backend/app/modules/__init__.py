# -*- coding: utf-8 -*-

import logging
from importlib import import_module
from os import listdir, getcwd
from os.path import isdir

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


def init_app(app, **kwargs):
    modules = app.config.get('APP_MODULES')
    if not modules:
        path = getcwd() + '/app/modules/'
        modules = [module_name for module_name in
            (m[:-3] if m[-3:] == '.py' else m for m in listdir(path)
            if m not in ['__pycache__',  '__init__.py'] and
            (isdir(path + m) or m[-3:] == '.py'))]

    for module_name in modules:
        try:
            logging.info('Loading \'%s\' module models', module_name)
            import_module('.%s.models' % module_name, package=__name__)
        except ImportError:
            logging.exception('Error loading \'%s\' module models', module_name)

    for module_name in modules:
        logging.info('Loading \'%s\' module', module_name)
        module = import_module('.%s' % module_name,
                               package=__name__)

        if hasattr(module, 'init_app'):
            module.init_app(app, **kwargs)
        else:
            logging.warning('Module \'%s\' has no init_app()', module_name)
