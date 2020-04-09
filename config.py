import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False  #for whoosh to enable signals, set false if no full text search
PER_PAGE = 20
DEBUG = True
SECRET_KEY = 's3cr3t'
UPLOADED_IMAGES_DEST =  BASE_DIR + '/app/static/uploads/img'
#UPLOADED_IMAGES_ALLOWED = ('png', 'jpg', 'jpeg', 'gif', 'svg')
UPLOADED_ATTACHMENTS_DEST = BASE_DIR + '/app/static/uploads/attachments'
#UPLOADED_ATTACHMENTS_ALLOWED = ('pdf', 'doc', 'docx')
