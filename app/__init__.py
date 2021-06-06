from flask import Flask 
from config import config_options
from flask_bootstrap import Bootstrap

#initializing bootstrap extension
bootstrap = Bootstrap()

def create_app(config_name):

    #initializing application
    app= Flask(__name__,instance_relative_config =True)

    #creating configurations
    app.config.from_object(config_options[config_name])
    
    #initialize flask extensions
    bootstrap.init_app(app)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #Set up configurations
    from .requests import configure_request
    configure_request(app)

    return app