
# # import os, sys
# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# from flask import Flask, render_template
# from flask_debugtoolbar import DebugToolbarExtension
# from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface

# app = Flask(__name__)
# app.debug = True
# app.config['SECRET_KEY'] = 'nlanblanlaalsldajsao'
# toolbar = DebugToolbarExtension(app)
# app.config['DEBUG_TB_PANELS'] += ('flask.ext.mongoengine.panels.MongoDebugPanel',)
# app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
# # app.config.from_pyfile('config.cfg')
# app.config['MONGODB_SETTINGS'] = {'DB': 'biomics'}
# db = MongoEngine(app)
# app.session_interface = MongoEngineSessionInterface(db)

# @app.route('/')
# def index():
# 	# todo = db.objects.get_or_404(_id=1)
#     return render_template('404.jade')

# @app.route('/<collection>')
# def collection(collection):
# 	if collection in DOMAIN.keys():
# 		pass
# 	abort(404)

# if __name__ == "__main__":
#         # app.debug = True
#         app.run(host="0.0.0.0", port=5000)

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()