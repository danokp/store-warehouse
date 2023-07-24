import dj_database_url
import os

from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'true').lower() in {'yes', '1', 'true'}
MODE = os.getenv('MODE')
SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME')
DATABASE_URL = dj_database_url.config(conn_max_age=600)
STORE_WAREHOUSE_SYNC_URL = os.getenv('STORE_WAREHOUSE_SYNC_URL')
CLIENT_URL = os.getenv('CLIENT_URL')
