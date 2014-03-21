#!/usr/bin/env python
# encoding:utf-8
from commands import Encode, Roadmap, Tcga
from flask import Flask, render_template

# # # Set the path
# import os, sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # from flask.ext.script import Manager, Server
# # # from tumblelog import app

# from flaskext.actions import Manager

# manager = Manager(app)

# # Turn on debugger by default and reloader
# manager.add_command("runserver", Server(
#     use_debugger = True,
#     use_reloader = True,
#     host = '0.0.0.0')
# )

# follw this example: https://github.com/mitsuhiko/flask/tree/master/examples/flaskr/

from flask.ext.script import Manager # http://flask-script.readthedocs.org/en/latest/
from flask.ext.mongoengine import MongoEngine # https://flask-mongoengine.readthedocs.org/en/latest/

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'local'}
db = MongoEngine(app)

# import pyjade to Flask
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

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

