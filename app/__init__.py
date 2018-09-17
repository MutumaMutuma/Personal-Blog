from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_mail import Mail


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()

bootstrap = Bootstrap()

db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    bootstrap = Bootstrap(app)
    login_manager.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # registering the main app blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    # configure UploadSet
    configure_uploads(app,photos)

    return app 