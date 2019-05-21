# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app, APP_MODE_CLI

__author__ = 'Alexey Kachalov <kachalov@kistriver.com>'


app = create_app(mode=APP_MODE_CLI)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
