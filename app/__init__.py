import os

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import app_config

app = Flask(__name__)
config_name = os.getenv('FLASK_CONFIG')
app.config.from_object(app_config[config_name])

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
ma = Marshmallow(app)
api = Api(app)

from .resources import PlayerAllResource, PlayerResource
api.add_resource(PlayerAllResource, "/players")
api.add_resource(PlayerResource, "/player")
