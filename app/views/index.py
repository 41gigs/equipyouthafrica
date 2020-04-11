from flask import Blueprint, render_template, g, request, flash, redirect

from ..models import Setting, Page, Link, Subject, Video, Post, Message, Gallery
from ..forms import MessageForm
from ..extensions import db

bp = Blueprint('index', __name__)

@bp.before_request
def load_settings_func():
    app = {}
    app_name = Setting.query.filter_by(key='APPLICATION_NAME').first()
    if app_name:
        app['NAME'] = app_name.value

    app_logo_light = Setting.query.filter_by(key='APPLICATION_LOGO_LIGHT').first()
    if app_logo_light.image:
        app['LOGO_LIGHT'] = app_logo_light.imgsrc

    app_logo_dark = Setting.query.filter_by(key='APPLICATION_LOGO_DARK').first()
    if app_logo_dark.image:
        app['LOGO_DARK'] = app_logo_dark.imgsrc 

    whatsapp= Setting.query.filter_by(key='WHATSAPP').first()
    if whatsapp:
        app['WHATSAPP'] = whatsapp.value

    facebook= Setting.query.filter_by(key='FACEBOOK').first()
    if facebook:
        app['FACEBOOK'] = facebook.value


    links = Link.query.all()
    contacts = {}
    courses = Subject.query.order_by(Subject.priority.desc()).limit(4)
    if courses:
        app['TOP_COURSES'] = courses

    settings = {'APPLICATION_NAME': app_name.value if app_name else None,
            'CONTACTS': contacts,
            'COURSES': courses}
    g.settings = settings
    g.application = app

@bp.route('/', methods=['GET', 'POST'])
def root():
    root = {}
    
    hero_image_setting = Setting.query.filter_by(key='HERO_IMAGE').first()
    hero_image = None
    if hero_image_setting and hero_image_setting.image:
        hero_image = hero_image_setting.imgsrc

    landing_image_1=None
    landing_image_1_setting = Setting.query.filter_by(key='LANDING_IMAGE_1').first()
    if landing_image_1_setting.image:
        landing_image_1 = landing_image_1_setting.imgsrc

    landing_image_2 = None
    landing_image_2_setting = Setting.query.filter_by(key='LANDING_IMAGE_2').first()
    if landing_image_2_setting.image:
        landing_image_2  = landing_image_2_setting.imgsrc
    landing_heading_1 = None

    landing_heading_1_setting = Setting.query.filter_by(key='LANDING_HEADING_1').first()
    if landing_heading_1_setting:
        landing_heading_1 = landing_heading_1_setting.value

    landing_text_1 = None
    landing_text_1_setting = Setting.query.filter_by(key='LANDING_TEXT_1').first()
    if landing_text_1_setting:
        landing_text_1 = landing_text_1_setting.value

    landing_heading_2_setting = Setting.query.filter_by(key='LANDING_HEADING_2').first()
    if landing_heading_2_setting:
        landing_heading_2 = landing_heading_2_setting.value

    landing_text_2 = None
    landing_text_2_setting = Setting.query.filter_by(key='LANDING_TEXT_2').first()
    if landing_text_2_setting:
        landing_text_2 = landing_text_2_setting.value

    
    landing_heading_3_setting = Setting.query.filter_by(key='LANDING_HEADING_3').first()
    if landing_heading_3_setting:
        landing_heading_3 = landing_heading_3_setting.value

    landing_text_3 = None
    landing_text_3_setting = Setting.query.filter_by(key='LANDING_TEXT_3').first()
    if landing_text_3_setting:
        landing_text_3 = landing_text_3_setting.value

    landing_heading_4_setting = Setting.query.filter_by(key='LANDING_HEADING_4').first()
    if landing_heading_4_setting:
        landing_heading_4 = landing_heading_4_setting.value

    landing_text_4 = None
    landing_text_4_setting = Setting.query.filter_by(key='LANDING_TEXT_4').first()
    if landing_text_4_setting:
        landing_text_4 = landing_text_4_setting.value

    #courses = Subject.query.order_by(Subject.priority).limit(4)
    videos = Video.query.limit(2)
    form = MessageForm()

    if form.validate_on_submit():
        message_to_add = Message(name=form.name.data, email=form.email.data, text=form.text.data)
        db.session.add(message_to_add)
        db.session.commit()
        flash('Your message has been sent', 'blue')
        return redirect(request.url)

    return render_template('index.html',  
            HERO_IMAGE=hero_image,
            LANDING_IMAGE_1=landing_image_1,
            LANDING_IMAGE_2=landing_image_2, 
            LANDING_HEADING_1=landing_heading_1,
            LANDING_TEXT_1=landing_text_1,
            LANDING_HEADING_2=landing_heading_2,
            LANDING_TEXT_2=landing_text_2,
            LANDING_HEADING_4=landing_heading_4,
            LANDING_TEXT_4=landing_text_4,
            LANDING_HEADING_3=landing_heading_3,
            LANDING_TEXT_3=landing_text_3,
            videos=videos, 
            form=form)

@bp.route('/page/<slug>')
def page(slug):
    page = Page.query.filter_by(slug=slug).first_or_404()
    courses = Subject.query.order_by(Subject.priority).limit(3)

    return render_template('page.html', page=page, courses=courses)

@bp.route('/courses')
def courses():
    courses = Subject.query.order_by(Subject.priority.desc()).paginate(1, 20, False)
    return render_template('courses.html', courses=courses.items)

@bp.route('/fees-structure')
def fees():
    courses = Subject.query.order_by(Subject.priority.desc()).paginate(1, 20, False)
    return render_template('fees.html', courses=courses.items)


@bp.route('/courses/<slug>')
def course(slug):
    course = Subject.query.filter_by(slug=slug).first_or_404()
    courses = Subject.query.order_by(Subject.priority.desc()).limit(3)

    return render_template('course.html', course=course, courses=courses)

@bp.route('/blog')
def blog():
    posts= Post.query.order_by(Post.modified.desc()).paginate(1,10, False)
    return render_template('blog.html', posts=posts.items)

@bp.route('/blog/<slug>')
def post(slug):
    post= Post.query.filter_by(slug=slug).first_or_404()
    return render_template('post.html', post=post)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    results = None
    if request.method == 'POST':
        results = Subject.query.filter(Subject.title.like('%' + request.form['search'] + '%')).all()
        
    return render_template('courses.html', courses=results)

@bp.route('/gallery')
def gallery():
    gallery = Gallery.query.paginate(1, 10, False)

    return render_template('gallery.html', gallery=gallery.items)
