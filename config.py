#this is the configuration file to configure flask to the app location & variables needed to run Flask


import os #operating system 
from dotenv import load_dotenv #allows us to load the environment variables (variables needed to run application)


# establish the base directory so whenever we use "." to reference any location in the app it knows we are referencing
# GameOfThrones_collection folder 
basedir = os.path.abspath(os.path.dirname(__file__))


#need to establish where the environment variables are coming from (this file will be hidden from github)
load_dotenv(os.path.join(basedir, '.env'))



#create the Config class 
class Config():

    """
    Create Config class which will setup the configuration variables.
    Using Environment variables where available other create config variables. 
    """


    FLASK_APP = os.environ.get('FLASK_APP') #looking for key of FLASK_APP in the environment variable location (.env)
    FLASK_ENV = os.environ.get('FLASK_ENV') 
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Literally whatever you want as long as its a string. Cool Beans'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # dont want a messsage every single time the database changes