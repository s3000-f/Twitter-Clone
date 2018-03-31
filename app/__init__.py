from flask import Flask
from flask_cors import CORS

from app.api import api_rest, api_bp
from app.client import client_bp

app = Flask(__name__, static_url_path='')
CORS(app)
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)

from . import config
app.logger.info('>>> {}'.format(app.config['MODE']))
