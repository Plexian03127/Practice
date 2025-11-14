from flask import Flask
from flask_dotenv import DotEnv

def create_app():
    app = Flask(__name__)
    env = DotEnv()
    env.init_app(app)
    
    from .routes import bp
    app.register_blueprint(bp)
    return app