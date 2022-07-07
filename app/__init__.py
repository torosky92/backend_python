from flask import Flask
from flask_talisman import Talisman
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_cors import CORS
from configure.Config import Config
from configure.PglConfig import PglConfig

#Flask App Configuration
app = Flask(__name__)
CORS(app)
Talisman(app)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})
CORS(app)
app.config.from_object(Config)

# Postgres import configurarion
app.config.from_object(PglConfig)
db = SQLAlchemy(app)

from app.routes import Route

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=5000)