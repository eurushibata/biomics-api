#!/usr/bin/env python
# encoding:utf-8
from commands import Encode, Roadmap, Tcga
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

# # # Set the path
# import os, sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# follw this example: https://github.com/mitsuhiko/flask/tree/master/examples/flaskr/

from flask.ext.script import Manager # http://flask-script.readthedocs.org/en/latest/
from flask.ext.mongoengine import MongoEngine # https://flask-mongoengine.readthedocs.org/en/latest/

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'local'}
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

@app.route("/")
def hello():
	return render_template('index.jade')
    # return "Hello World!"

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

