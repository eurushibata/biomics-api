# -*- coding: utf-8 -*-

from flask import Flask, render_template

# from flask.ext.babel import Babel # i18n

def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)
    # configure_app(app, config)
    # configure_hook(app)
    # configure_blueprints(app, blueprints)
    # configure_extensions(app)
    # configure_logging(app)
    # configure_template_filters(app)
    configure_error_handlers(app)

    return app


def configure_error_handlers(app):

	@app.errohandler(403)
	def forbidden_page(error):
		return render_template("errors/403.jade"), 403

	@app.errohandler(404)
	def page_not_found(error):
		return render_template("errors/404.jade"), 404

	@app.errohandler(500)
	def server_error_page(error):
		return render_template("errors/500.jade"), 500