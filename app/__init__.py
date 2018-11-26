# import necessary files
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# set appilication variables, app variables must be set first
app = Flask(__name__)

# set config variables for this appilication
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) # migrate class needs to know which app and db instance to use
bootstrap = Bootstrap(app)

# import routes
from app import routes
