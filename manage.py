# # # Set the path
# import os, sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # from flask.ext.script import Manager, Server
# # # from tumblelog import app
# from flask import Flask
# from flaskext.actions import Manager

# manager = Manager(app)

# # Turn on debugger by default and reloader
# manager.add_command("runserver", Server(
#     use_debugger = True,
#     use_reloader = True,
#     host = '0.0.0.0')
# )

# if __name__ == "__main__":
#     manager.run()


#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

from flask import Flask
from flaskext.actions import Manager
import settings
from test import app

app.config.from_object(settings)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()

