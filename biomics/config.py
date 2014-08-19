# -*- coding: utf-8 -*-

import os

from utils import make_dir, INSTANCE_FOLDER_PATH

class BaseConfig(object):

    PROJECT = 'biOMICs'

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = False
    TESTING = False

    ADMINS = ['urushibata.emerson@gmail.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'G3cw{uuw`_^81IktN6a5(3/O&l?fU[5l'

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    make_dir(LOG_FOLDER)

    TEMPLATE_FOLDER_PATH = os.path.join(PROJECT_ROOT, 'biomics', 'templates')
    STATIC_FOLDER_PATH = os.path.join(PROJECT_ROOT, 'biomics', 'static')

class DefaultConfig(BaseConfig):

    DEBUG = False

    # Flask-babel: http://pythonhosted.org/Flask-Babel/
    # ACCEPT_LANGUAGES = ['pt-br']
    BABEL_DEFAULT_LOCALE = 'en'

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    # Flask-mail: http://pythonhosted.org/flask-mail/
    # https://bitbucket.org/danjac/flask-mail/issue/3/problem-with-gmails-smtp-server
    MAIL_DEBUG = DEBUG
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Should put MAIL_USERNAME and MAIL_PASSWORD in production under instance folder.
    MAIL_USERNAME = 'biomics.dev@gmail.com'
    MAIL_PASSWORD = 'biomicsdev'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    # # Flask-openid: http://pythonhosted.org/Flask-OpenID/
    # OPENID_FS_STORE_PATH = os.path.join(INSTANCE_FOLDER_PATH, 'openid')
    # make_dir(OPENID_FS_STORE_PATH)

    DB_NAME = 'test'
    DB_USERNAME = 'admin'
    DB_PASSWORD = 'test'
    DB_HOST = 'localhost'
    DB_PORT = 27017

class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False