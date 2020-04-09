# third party imports
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

# local imports
from .models import User
from .extensions import images, attachments, IMAGES, ATTACHMENTS

class JoinForm(Form):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Full Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Repeat Password', validators=[DataRequired()])

    def validate_email(self, field):   
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already taken')

class LoginForm(Form):
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

class SubjectForm(Form):
    title = StringField('Name', validators=[DataRequired()])
    body= TextAreaField('Content', validators=[DataRequired()])
    fees = StringField('Fees (Ugx)')
    image = FileField('Cover Image', validators=[FileAllowed(IMAGES, 'Images only!')])
    image_external = StringField('External image')
    image_caption = StringField('Caption')
    priority = StringField('Priority', description='Higher values show up first in the list ')
    meta_description = TextAreaField('Meta Description')

class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Content', validators=[DataRequired()])
    meta_description = TextAreaField('Meta Description')
    tags = StringField('Tags')
    image =FileField('Cover Image', validators=[FileAllowed(IMAGES, 'Images only!')])
    image_external = StringField('External image')
    image_caption = StringField('Caption')

class PageForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Content', validators=[DataRequired()])
    meta_description = TextAreaField('Meta Description')
    image_external = StringField('External Image')
    image =FileField('Cover Image', validators=[FileAllowed(IMAGES, 'Images only!')])
    image_caption = StringField('Caption')
    attachment =FileField('Attachemnt', validators=[FileAllowed(ATTACHMENTS, 'Office documents and PDF only!')])
    attachment_caption = StringField('Caption')

class GalleryForm(Form):
    #key = StringField('Name', validators=[DataRequired()])
    caption = StringField('Caption')
    image = FileField('Image', validators=[FileAllowed(IMAGES, 'Images only!')])

class SettingForm(Form):
    key = StringField('Name', validators=[DataRequired()])
    value = StringField('Value')
    image = FileField('Image', validators=[FileAllowed(IMAGES, 'Images only!')])

class VideoForm(Form):
    youtube_id = StringField('Youtube ID', validators=[DataRequired()])

class LinkForm(Form):
    title = StringField('Label', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])

class MessageForm(Form):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    text = StringField('Message', validators=[DataRequired()])
