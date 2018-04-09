import os

from api import create_app

config_name = os.getenv('APP_SETTINGS', 'production')
app = create_app(config_name)