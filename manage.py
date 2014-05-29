#!/usr/bin/env python
# encoding:utf-8
from commands import Encode, Roadmap, Tcga
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension


# follow this example: https://github.com/mitsuhiko/flask/tree/master/examples/flaskr/

from flask.ext.script import Manager # http://flask-script.readthedocs.org/en/latest/
from flask.ext.mongoengine import MongoEngine # https://flask-mongoengine.readthedocs.org/en/latest/

try:
    from settings import *
except ImportError:
    print u'Warning: local_settings not found'

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'DB':DB_NAME,
    'USERNAME':DB_USERNAME,
    'PASSWORD':DB_PASSWORD,
    'HOST':DB_HOST,
    'PORT':DB_PORT
}

db = MongoEngine(app)

# import pyjade to Flask
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# the toolbar is only enabled in debug mode:
app.debug = True
app.config['SECRET_KEY'] = 'G3cw{uuw`_^81IktN6a5(3/O&l?fU[5l'

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


manager = Manager(app)


@app.route('/')
def index():
	return render_template('index.jade')

@app.route('/terms/')
@app.route('/terms')
def terms():
    return render_template('terms.jade')

@app.route('/terms/<path:path>/')
def term(path):
    return render_template('term.jade', path=path)

@manager.command
def dbdump():
	"Dump dataset database"

	print "Dump"

@manager.command
def init_db():
	"Creates de database tables."
	print "Dump"

@manager.command
def init_db():
	"Updates de database entries."
	print "Dump"

manager.add_command("encode", Encode())
manager.add_command("roadmap", Roadmap())
manager.add_command("tcga", Tcga())

if __name__ == "__main__":
    manager.run()

