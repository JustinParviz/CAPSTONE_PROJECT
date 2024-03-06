from flask import Flask
from flask_migrate import Migrate 

#internal imports 
from .blueprints.site.routes import site
from .blueprints.auth.routes import auth
from config import Config
from .models import login_manager, db


#instantiating the Flask app
app = Flask(__name__) #passing in the __name__ variable which just takes the name of the folder we're in
app.config.from_object(Config)


#wrap the app in login_manager so it can be used wherever in the app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in' 
login_manager.login_message = "Hey you! Log in please!"
login_manager.login_message_category = 'warning'


#we are going to use a decorator to create our first route
#@app.route("/")
#def hello_world():
#    return "<p>Hello World!</p>"

# We can also comment out the above because this is rendering to the same
# location as our site blueprint. 


app.register_blueprint(site) # add this here to register the site blueprint
app.register_blueprint(auth)


#instantiating the datbase & wrapping the app
db.init_app(app)
migrate = Migrate(app, db)



