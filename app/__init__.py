from flask import Flask 

#initializing application
app= Flask(__name__)

#Set up configurations
app.config.from_object(DevConfig)
from app import views