# import necessary files
from flask import Flask
from flask_bootstrap import Bootstrap


# set appilication variables, app variables must be set first
app = Flask(__name__)
bootstrap = Bootstrap(app)

# import routes
from app import routes
