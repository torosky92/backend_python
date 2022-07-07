import os
from sqlalchemy.pool import QueuePool

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
DEBUG = os.environ.get('FLASK_DEBUG', False)

class PglConfig(object):
    user=os.environ.get('POSTGRES_USER')
    password=os.environ.get('POSTGRES_PASSWORD')
    db=os.environ.get('POSTGRES_DB')
    host=os.environ.get('HOST_DATA')
    port=os.environ.get('POSTGRES_PORT')
    ssl_context='adhoc'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}/{db}'
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'poolclass': QueuePool,
        'pool_size' : 90
    }
