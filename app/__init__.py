#third party imports
from flask import Flask

# local imports
from .extensions import db, migrate, login_manager, mail, upload_manager

def create_app(config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('settings.py') #in instance, sensitive stuff

    from .filters import register_filters
    register_filters(app)

    initialize(app)
    blueprints(app)

    return app

def initialize(app):
    db.init_app(app)
    mail.init_app(app)
    
    login_manager.session_protection = 'strong'
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    upload_manager(app)

    from .models import User 
    migrate.init_app(app, db)


def blueprints(app):
    
    from .views.index import bp as main
    from .views.dashboard import bp as dashboard
    from .views.auth import bp as auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard, url_prefix='/dashboard')
    
