# import necessary files
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config


# set appilication variables, app variables must be set first
app = Flask(__name__)

# set config variables for this appilication
app.config.from_object(Config)

bootstrap = Bootstrap(app)

# import routes
from app import routes
