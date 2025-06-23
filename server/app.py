from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config


db = SQLAlchemy()
migrate = Migrate()   # Initialize extensions
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize extensions with app
    jwt.init_app(app)
    CORS(app)
    
    
    from models import User, Guest, Episode, Appearance
    
   
    from controllers.auth_controller import auth_bp
    from controllers.guest_controller import guest_bp
    from controllers.episode_controller import episode_bp
    from controllers.appearance_controller import appearance_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)
    
    @app.route('/')
    def index():
        return {
            'message': 'Welcome to Late Night TV Show API',
            'version': '1.0.0',
            'endpoints': {
                'auth': ['/register', '/login'],
                'episodes': ['/episodes', '/episodes/<id>'],
                'guests': ['/guests'],
                'appearances': ['/appearances']
            }
        }
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)