from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, patch_request_class
IMAGES =('jpg', 'png', 'svg', 'jpeg', 'gif') 
ATTACHMENTS = ('doc', 'pdf', 'xls')

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
images = UploadSet('images')
attachments = UploadSet('attachments', ATTACHMENTS)

def upload_manager(app):
    configure_uploads(app, (images, attachments))
    patch_request_class(app, 32 * 1024 * 1024) #max size 32MB
