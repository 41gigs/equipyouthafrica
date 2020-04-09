# third party imports
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from slugify import slugify
from markdown import markdown
import bleach
import uuid
import datetime

# local imports
from .extensions import db, login_manager, images, attachments

allowed_tags = ['a', 'b', 'blockqoute', 'i','br', 'ul', 'li', 'ol', 'h1', 'h2','h3', 'p', 'strong', 'em']

""" User Roles """
ROLES = {
        'user': 1,
        'editor':2,
        'manager':3,
        'admin': 4,                                                                                                        'developer':5
        }

def generate_uuid():
    return str(uuid.uuid4().hex)[:8]

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)     
    uid = db.Column(db.String, unique=True, default=generate_uuid)
    slug = db.Column(db.String)   
    created = db.Column(db.DateTime, default = db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'), tags=allowed_tags, strip=True))

class User(Base, UserMixin):
    __tablename__ = 'users'

    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    about_me = db.Column(db.String)
    last_seen = db.Column(db.DateTime, default=db.func.current_timestamp())
    password = db.Column(db.String)
    confirmed=db.Column(db.Boolean, default=False)
    confirmed_on = db.Column(db.DateTime)
    image = db.Column(db.String)
    role = db.Column(db.Integer, default= ROLES['user'])
    pages = db.relationship('Page', backref='author', lazy='dynamic')  
    posts = db.relationship('Post', backref='author', lazy='dynamic')   
    subjects = db.relationship('Subject', backref='author', lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(self.password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def is_admin(self):
        return self.role == ROLES['admin']

    def is_allowed(self, access_level):
        return self.role >= access_level

    def __repr__(self):
        return '<User {}>'.format(self.id)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Subject(Base):
    __tablename__ = 'subjects'

    title = db.Column(db.String)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)    
    fees= db.Column(db.String)
    image = db.Column(db.String)
    image_caption = db.Column(db.String)
    image_external= db.Column(db.String) 
    priority = db.Column(db.Integer, default=0)
    meta_description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))  

    @property
    def imgsrc(self):
        return images.url(self.image)

    def __repr__(self):
        return '<Subject {}>'.format(self.title)

db.event.listen(Subject.title, 'set', Subject.generate_slug, retval=False)
db.event.listen(Subject.body, 'set', Subject.on_changed_body)

class Tag(Base):
    __tablename__ = 'tags'

    title = db.Column(db.String)

    def __repr__(self):
        return '<Tag {}'.format(self.id)

db.event.listen(Tag.title, 'set', Tag.generate_slug, retval=False)

post_tags = db.Table('post_tags',
        db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
        db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')) 
        )

class Post(Base):
    __tablename__ = 'posts'

    title = db.Column(db.String)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    image = db.Column(db.String)
    image_caption = db.Column(db.String)
    image_external= db.Column(db.String)
    meta_description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    tags = db.relationship('Tag',
            secondary= post_tags, 
            backref=db.backref('posts', lazy='dynamic'))

    def set_tags(self, tags):
        """ Add tags from csv list """
        self.tags = []
        for tag in [t.strip() for t in tags.split(', ')]:
            self.tags.append(Tag(title=tag))

    @property
    def imgsrc(self):
        return images.url(self.image)

    @property
    def taglist(self):
        """ Convert tags to csv list """
        tags = []
        for tag in self.tags:
            tags.append(tag.title)
        return ', '.join(map(str, tags))
    
    def __repr__(self):
        return '<Post {}>'.format(self.id)

db.event.listen(Post.title, 'set', Post.generate_slug, retval=False)
db.event.listen(Post.body, 'set', Post.on_changed_body)


class Page(Base):
    __tablename__ = 'pages'

    title = db.Column(db.String)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    image = db.Column(db.String)
    image_caption = db.Column(db.String)
    image_external= db.Column(db.String)
    attachment = db.Column(db.String)
    attachment_caption = db.Column(db.String)
    meta_description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

    @property
    def imgsrc(self):
        return images.url(self.image)
    @property
    def attachmentsrc(self):
        return attachments.url(self.attachment)

    def __repr__(self):
        return '<Page {}>'.format(self.id)

db.event.listen(Page.title, 'set', Page.generate_slug, retval=False)
db.event.listen(Page.body, 'set', Page.on_changed_body)

class Attachment(Base):
    __tablename__ = 'attachments'

    name = db.Column(db.String)
    filename = db.Column(db.String)

    def __repr__(self):
        return '<Attachment {}>'.format(self.id)

class Link(Base):
    __tablename__ = 'links'

    title = db.Column(db.String)
    url = db.Column(db.String)

db.event.listen(Link.title, 'set', Link.generate_slug, retval=False)

class Video(Base):

    __tablename__ = 'videos'

    youtube_id = db.Column(db.String)

class Setting(Base):

    __tablename__ = 'settings'

    key = db.Column(db.String)
    value = db.Column(db.String)
    image = db.Column(db.String)

    @property
    def imgsrc(self):
        return images.url(self.image)

    def __repr__(self):
        return '<Setting {}'.format(self.id)

class Gallery(Base):

    __tablename__ = 'gallery'

    caption = db.Column(db.String)
    image = db.Column(db.String)

    @property
    def imgsrc(self):
        return images.url(self.image)

    def __repr__(self):
        return '<Gallery {}'.format(self.id)

class Message(Base):

    __tablename__ = 'messages'

    name = db.Column(db.String)
    email = db.Column(db.String)
    text = db.Column(db.String)
    read = db.Column(db.Boolean)

    def __repr__(self):
        return '<Message {}'.format(self.id)

