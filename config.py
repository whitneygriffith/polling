#configuration file for votr
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'tutpolling.db')
SECRET_KEY = 'development key' # keep this key secret during production
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://admin1234@tutpolling:@Qwerty1234@tutpolling.mysql.database.azure.com/tutpolling'.format(DB_PATH)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True