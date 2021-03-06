import os
from dotenv import load_dotenv

from flask import Flask
from flask_migrate import Migrate

from app import create_app
from app.extensions import DB

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

flask_app: Flask = create_app(os.getenv('FLASK_ENV') or 'default')
migrate: Migrate = Migrate(flask_app, DB)