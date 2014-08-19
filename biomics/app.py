# -*- coding: utf-8 -*-

import os

from flask import Flask, request, render_template
from flask.ext.babel import Babel
from flask_debugtoolbar import DebugToolbarExtension

from .config import DefaultConfig
from .extensions import mail, cache, db
from .frontend import frontend
from .utils import INSTANCE_FOLDER_PATH


# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    frontend,
)


def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, 
                instance_path=INSTANCE_FOLDER_PATH,
                instance_relative_config=True,
                template_folder=DefaultConfig.TEMPLATE_FOLDER_PATH,
                static_folder=DefaultConfig.STATIC_FOLDER_PATH)
    configure_app(app, config)
    # configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_db(app)
    configure_extensions(app)
    configure_logging(app)
    # configure_template_filters(app)
    configure_error_handlers(app)

    return app

def configure_app(app, config=None):
    """Different ways of configurations."""

    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    # http://flask.pocoo.org/docs/config/#instance-folders
    app.config.from_pyfile('production.cfg', silent=True)

    if config:
        app.config.from_object(config)

    # Use instance folder instead of env variables to make deployment easier.
    #app.config.from_envvar('%s_APP_CONFIG' % DefaultConfig.PROJECT.upper(), silent=True)


def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_db(app):
    app.config['MONGODB_SETTINGS'] = {
        'DB': DefaultConfig.DB_NAME,
        'USERNAME': DefaultConfig.DB_USERNAME,
        'PASSWORD': DefaultConfig.DB_PASSWORD,
        'HOST': DefaultConfig.DB_HOST,
        'PORT': DefaultConfig.DB_PORT
    }
    db.init_app(app)

def configure_extensions(app):

    # the toolbar is only enabled in debug mode:
    app.debug = DefaultConfig.DEBUG
    app.config['SECRET_KEY'] = DefaultConfig.SECRET_KEY

    app.config['DEBUG_TB_PANELS'] = [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        # 'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        # Add the MongoDB panel
        'flask.ext.mongoengine.panels.MongoDebugPanel',
    ]

    toolbar = DebugToolbarExtension(app)

    # pyjade to Flask
    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    # flask-mail
    mail.init_app(app)

    # flask-cache
    cache.init_app(app)

    # flask-babel
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        accept_languages = app.config.get('ACCEPT_LANGUAGES')
        return request.accept_languages.best_match(accept_languages)


def configure_logging(app):
    """Configure file(info) and email(error) logging."""

    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    import logging
    from logging.handlers import SMTPHandler

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
    info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)

    # Testing
    # app.logger.info("testing info.")
    # app.logger.warn("testing warn.")
    # app.logger.error("testing error.")
    

    mail_handler = SMTPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                               app.config['MAIL_USERNAME'],
                               app.config['ADMINS'],
                               'O_ops... %s failed!' % app.config['PROJECT'],
                               (app.config['MAIL_USERNAME'],
                                app.config['MAIL_PASSWORD']))
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(mail_handler)


def configure_error_handlers(app):

	@app.errorhandler(403)
	def forbidden_page(error):
		return render_template("errors/403.jade"), 403

	@app.errorhandler(404)
	def page_not_found(error):
		return render_template("errors/404.jade"), 404

	@app.errorhandler(500)
	def server_error_page(error):
		return render_template("errors/500.jade"), 500