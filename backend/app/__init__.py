from flask import Flask , request, jsonify

from flask_cors import CORS
from flask_mongoengine import MongoEngine

#Global accessible library
# user_collection = mongo.db.users

#Re- initialize database
my_mongo_db = MongoEngine()


def create_app():
    """Create Flask Application = Core Application""" 
    app = Flask(__name__, instance_relative_config=False) 
    CORS(app)
    cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
    })
    app.config.from_pyfile('../config.py')
  
  
    #Initialize Plugins 
    """Initializing plugins sets global variables makes them 
    globally accesible via other parts of our application """
    my_mongo_db.init_app(app)
    

    with app.app_context(): 
        #Import parts of application 
        from .api.home.routes import home_bp
        from .api.file_handler.routes import file_bp

        #Register Blueprints
        app.register_blueprint(home_bp)
        app.register_blueprint(file_bp)

    return app 



