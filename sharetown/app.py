import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from flask import request, redirect
from flask.ext.assets import Environment, Bundle
from flask.ext.babel import Babel, format_datetime
from urlparse import urlparse, urlunparse
from .routes import index

APP_ROOT        = os.path.abspath(os.path.dirname(__file__))
APP_CONFIG_ROOT = os.path.join(APP_ROOT, 'configs')
APP_STATIC_ROOT = os.path.join(APP_ROOT, 'statics')

def create_app(config=None):
	app = Flask(__name__, static_folder='statics', template_folder='templates')
	app.jinja_env.trim_blocks = True

	app.config.from_pyfile(os.path.join(APP_CONFIG_ROOT, 'default.py'))

	assets = Environment()
	assets.init_app(app)

	babel = Babel(app)

	app.register_blueprint(index.blueprint, url_prefix='')

	@app.template_filter('format_datetime')
	def format_datetime_filter(value, format = "yyyy-mm-dd HH:mm"):
		return format_datetime(value, format)

	# @app.before_request
	# def redirect_rhcloud():
	# 	urlparts = urlparse(request.url)
	# 	if urlparts.netloc == 'localhost:5000':
	# 		return redirect("http://share-donkey.rhcloud.com/", code=301)

	return app
