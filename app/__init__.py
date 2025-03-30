from flask import Flask
from app.routes import main
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register Blueprints
    app.register_blueprint(main)

    return app
