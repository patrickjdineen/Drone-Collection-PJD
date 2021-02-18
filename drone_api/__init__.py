from flask import Flask

#TODO: Import Config Opject for Flask Project
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Import for Flask Login
from flask_login import LoginManager

#import for authLib integrations
from authlib.integrations.flask_client import OAuth

from flask_marshmallow import Marshmallow

from flask_cors import CORS

#instantiation of classes from packages to be used across the application
app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'signin' #specifies what page to load for non authenticated users

ma = Marshmallow(app)

oauth = OAuth(app)

from drone_api import routes, models