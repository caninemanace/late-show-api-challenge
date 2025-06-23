from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Import models to register them with SQLAlchemy
    from models import User, Guest, Episode, Appearance
    
    # Register controllers/blueprints
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