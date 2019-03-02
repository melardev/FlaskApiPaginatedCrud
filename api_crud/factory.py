import os

from config import DevConfig
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# config = DevConfig if get_debug_flag() else ProdConfig
config = DevConfig

app = Flask(__name__, root_path=os.getcwd())
app.config.from_object(config)

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# cors with defaults, which means allow all domains, it is fine for the moment
cors = CORS(app)
