from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask import current_app as app
from flask_login import login_required
from slugify import slugify
import uuid
import os

# local imports
from ..forms import SubjectForm, PostForm, PageForm, SettingForm, LinkForm, VideoForm, GalleryForm, MessageForm
from ..models import Subject, Post, Tag, Page, Setting, Link, Video, Gallery, Message, ROLES
from ..extensions import db, images, attachments
from ..decorators import access_required

def unique_name():
    return str(uuid.uuid4().hex)[:8]

def generate_filename(value):
    return '{}-{}.'.format(slugify(value)[:55], unique_name())

def upload_image(name):
    if request.files['image']:
        return images.save(request.files['image'], name=generate_filename(name))
    return None

PER_PAGE = 20

bp = Blueprint('dashboard', __name__)

@bp.route('/')
@login_required
def root():
    return render_template('dashboard/root.html')

@bp.route('/courses')
@bp.route('/courses/<int:page>')
@login_required
def subject_list(page=1):
    """ List all subjects """
    subjects = Subject.query.order_by(Subject.modified.desc()).paginate(page, PER_PAGE, False)
    return render_template('dashboard/subject/list.html', subjects=subjects.items)

@bp.route('/courses/new', defaults={'uid': None}, methods=['GET', 'POST'])
@bp.route('/courses/edit/<uid>', methods=['GET', 'POST'])
@login_required
def subject_action(uid):
    """ Create or Edit a subject """
    subject = Subject.query.filter_by(uid=uid).first() if uid else None

    form = SubjectForm(obj = subject)

    if form.validate_on_submit():
        image = upload_image(form.title.data)
            
        if uid is None:
            subject_to_add = Subject(title=form.title.data,
                    body=form.body.data,
                    fees=form.fees.data,
                    priority=form.priority.data,
                    image=image,
                    image_external= form.image_external.data,
                    image_caption = form.image_caption.data,
                    meta_description=form.meta_description.data)
                       
            db.session.add(subject_to_add)
            flash('Course added', 'blue')
        else:
            subject.title = form.title.data
            subject.body = form.body.data
            subject.fees = form.fees.data
            subject.priority = form.priority.data
            subject.meta_description = form.meta_description.data
            subject.image_external = form.image_external.data
            subject.image_caption = form.image_caption.data
            
            if image and subject.image:
                os.remove(images.path(subject.image))
                
            subject.image = image

            flash('Course updated', 'blue')
        
        db.session.commit()
        return redirect(url_for('.subject_list'))

    return render_template('dashboard/subject/form.html', form=form, subject=subject) 

@bp.route('/courses/delete/<uid>', methods=['GET', 'POST'])
@login_required
def subject_delete(uid):
    subject = Subject.query.filter_by(uid=uid).first_or_404()
    if subject and subject.image:
        os.remove(images.path(subject.image))
    db.session.delete(subject)
    db.session.commit()
    flash('Course deleted', 'blue')
    return redirect(url_for('.subject_list'))

@bp.route('/posts')
@bp.route('/posts/<int:page>')
@login_required
def post_list(page=1):
    posts = Post.query.order_by(Post.modified.desc()).paginate(page, PER_PAGE, False)
    return render_template('dashboard/post/list.html', posts=posts.items)

@bp.route('/posts/new', defaults={'uid':None}, methods=['GET', 'POST'])
@bp.route('/posts/edit/<uid>', methods=['GET', 'POST'])
@login_required
def post_action(uid):
    """ Edit a post """
    post = Post.query.filter_by(uid=uid).first() if uid else None

    form = PostForm()

    if form.validate_on_submit():
        image = upload_image(form.title.data)

        if uid is None:
            post_to_add = Post(title=form.title.data,
                    body=form.body.data,
                    image=image,
                    meta_description= form.meta_description.data)
            post_to_add.set_tags(form.tags.data)
            db.session.add(post_to_add)
            flash('Post added', 'is-info')
        else:
            post.title = form.title.data
            post.body = form.body.data
            post.set_tags(form.tags.data)
            post.meta_description = form.meta_description.data
            
            if image and post.image:
                os.remove(images.path(post.image))
            
            post.image= image
                
            flash('Post Updated', 'is-info')
        db.session.commit()
        return redirect(url_for('.post_list'))
    if post:
        form.title.data = post.title
        form.body.data = post.body
        form.meta_description.data = post.meta_description
        form.tags.data = post.taglist
   
    return render_template('dashboard/post/form.html', form=form, post=post)

@bp.route('/posts/delete/<uid>', methods=['GET', 'POST'])
@login_required
def post_delete(uid):
    post = Post.query.filter_by(uid=uid).first()
    if post and post.image:
        os.remove(images.path(post.image))
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted', 'is-info')
    return redirect(url_for('.post_list'))


@bp.route('/pages')
@bp.route('/pages/<int:page>')
@login_required
def page_list(page=1):
    pages = Page.query.order_by(Page.modified.desc()).paginate(page, PER_PAGE, False)
    return render_template('dashboard/page/list.html', pages=pages.items)

@bp.route('/pages/new', defaults={'uid':None}, methods=['GET', 'POST'])
@bp.route('/pages/edit/<uid>', methods=['GET', 'POST'])
@login_required
def page_action(uid):
    page = Page.query.filter_by(uid=uid).first() if uid else None

    form = PageForm(obj = page)

    if form.validate_on_submit():
        image = upload_image(form.title.data)
        
        attachment = None
        if request.files['attachment']:
            attachment = attachments.save(request.files['attachment'])
         
        if uid is None:
            page_to_add = Page(title=form.title.data,
                    body=form.body.data,
                    image=image,
                    image_external = form.image_external.data,
                    image_caption = form.image_caption.data,
                    attachment=attachment,
                    attachment_caption = form.attachment_caption.data,
                    meta_description=form.meta_description.data)
            
            db.session.add(page_to_add)
            flash('Page Added', 'blue')
        else:
            page.title = form.title.data
            page.body = form.body.data
            page.meta_description = form.meta_description.data
            page.image_external = form.image_external.data
            page.image_caption = form.image_caption.data
            page.attachment_caption = form.attachment_caption.data

            if image and page.image:
                os.remove(images.path(page.image))
                
            page.image = image
            
            if attachment and page.attachment:
                os.remove(attachments.path(page.attachment))
                
            page.attachment = attachment

            flash('Page updated', 'blue')
        
        db.session.commit()
        return redirect(url_for('.page_list'))
    return render_template('dashboard/page/form.html', form=form, page=page)


@bp.route('/pages/delete/<uid>', methods=['GET', 'POST'])
@login_required
def page_delete(uid):
    page = Page.query.filter_by(uid=uid).first()
    if page and page.image:
        os.remove(images.path(page.image))
    if page and page.attachment:
        os.remove(attachments.path(page.attachment))
    db.session.delete(page)
    db.session.commit()
    flash('Page deleted', 'is-info')
    return redirect(url_for('.page_action', uid=uid))

@bp.route('/videos')
@bp.route('/videos/<int:page>')
@login_required
def video_list(page=1):
    videos = Video.query.order_by(Video.modified.desc()).paginate(page, PER_PAGE, False)
    return render_template('dashboard/video/list.html', videos=videos.items)

@bp.route('/videos/new', defaults={'uid':None}, methods=['GET', 'POST'])
@bp.route('/videos/edit/<uid>', methods=['GET', 'POST'])
@login_required
def video_action(uid):
    video = Video.query.filter_by(uid=uid).first() if uid else None

    form = VideoForm(obj=video)

    if form.validate_on_submit():
        if uid is None:
            video_to_add = Video(youtube_id=form.youtube_id.data)
            db.session.add(video_to_add)
            flash('Video Added', 'blue')
        else:
            video.youtube_id = form.youtube_id.data
            flash('Video updated', 'blue')
        db.session.commit()
        return redirect(url_for('.video_list'))

    return render_template('dashboard/video/form.html', form=form, video=video)

@bp.route('/videos/delete/<uid>', methods=['GET', 'POST'])
@login_required
def video_delete(uid):
    video = Video.query.filter_by(uid=uid).first()
    if video:
        db.session.delete(video)
        db.session.commit()
        flash('Video Deleted', 'blue')
    return redirect(url_for('.video_list'))

@bp.route('/links')
@bp.route('/links/<int:page>')
@login_required
def link_list(page=1):
    links = Link.query.order_by(Link.modified.desc()).paginate(page, PER_PAGE, False)
    return render_template('dashboard/link/list.html', links=links.items)

@bp.route('/links/new', defaults={'uid':None}, methods=['GET', 'POST'])
@bp.route('/links/edit/<uid>', methods=['GET', 'POST'])
@login_required
def link_action(uid):
    link = Link.query.filter_by(uid=uid).first() if uid else None

    form = LinkForm(obj=link)

    if form.validate_on_submit():
        if uid is None:
            link_to_add = Link(title=form.title.data, url = form.url.data)
            db.session.add(link_to_add)
            flash('Link added', 'blue')
        else:
            link.title = form.title.data
            link.url = form.url.data
            flash('Link Updated', 'blue')
        db.session.commit()
        return redirect(url_for('.link_list'))
    return render_template('dashboard/link/form.html', form=form, link=link)

@bp.route('/links/delete/<uid>', methods=['GET', 'POST'])
@login_required
def link_delete(uid):
    link = Link.query.filter_by(uid=uid).first()
    if link:
        db.session.delete(link)
        db.session.commit()
        flash('Link deleted', 'blue')
    return redirect(url_for('.link_list'))

@bp.route('/settings')
@bp.route('/settings/<int:page>')
@login_required
def setting_list(page=1):
    settings = Setting.query.paginate(page, PER_PAGE, False)
    return render_template('dashboard/setting/list.html', settings=settings.items)

@bp.route('/settings/new', defaults={'uid':None}, methods=['GET', 'POST'])
@bp.route('/settings/edit/<uid>', methods=['GET', 'POST'])
@login_required
def setting_action(uid):

    setting = Setting.query.filter_by(uid=uid).first() if uid else None
    form = SettingForm(obj=setting)

    if form.validate_on_submit():
        image = None
        if request.files['image']:
            image = upload_image(form.key.data)


        if uid is None:
            setting_to_add = Setting(key=form.key.data, value=form.value.data, image=image)
            db.session.add(setting_to_add)
            flash('Setting {} created successfully'.format(form.key.data), 'blue')
        else:
            setting.key = form.key.data
            setting.value = form.value.data
            
            if image and setting.image:
                os.remove(images.path(setting.image))
                
            setting.image = image
            flash('Setting {} updated successfully'.format(form.key.data), 'blue')
        db.session.commit()
        return redirect(url_for('.setting_list'))
    return render_template('dashboard/setting/form.html', form=form, setting=setting)

@bp.route('/settings/delete/<uid>', methods=['GET', 'POST'])
@login_required
def setting_delete(uid):
    setting = Setting.query.filter_by(uid=uid).first()
    if setting and setting.image:
        os.remove(images.path(setting.image))
    db.session.delete(setting)
    db.session.commit()
    flash('Setting Deleted', 'blue')
    return redirect(url_for('.setting_list'))

@bp.route('/gallery')
@bp.route('/gallery/<int:page>')
@login_required
def gallery_list(page=1):
    gallery = Gallery.query.paginate(page, PER_PAGE, False)
    return render_template('dashboard/gallery/list.html', gallery=gallery.items)

@bp.route('/gallery/new', defaults={'uid':None}, methods=['GET', 'POST'])
@bp.route('/gallery/edit/<uid>', methods=['GET', 'POST'])
@login_required
def gallery_action(uid):

    gallery = Gallery.query.filter_by(uid=uid).first() if uid else None
    form = GalleryForm(obj=gallery)

    if form.validate_on_submit():
        image = None
        if request.files['image']:
            image = images.save(request.files['image'], name=generate_filename(form.caption.data))


        if uid is None:
            gallery_to_add = Gallery(caption=form.caption.data, image=image)
            db.session.add(gallery_to_add)
            flash('Gallery  created successfully', 'blue')
        else:
            gallery.key = form.caption.data
                        
            if image and setting.image:
                os.remove(images.path(gallery.image))
                
            gallery.image = image
            flash('Gallery updated successfully', 'blue')
        db.session.commit()
        return redirect(url_for('.gallery_list'))
    return render_template('dashboard/gallery/form.html', form=form, gallery=gallery)

@bp.route('/gallery/delete/<uid>', methods=['GET', 'POST'])
@login_required
def gallery_delete(uid):
    gallery = Gallery.query.filter_by(uid=uid).first()
    if gallery and gallery.image:
        os.remove(images.path(gallery.image))
    db.session.delete(gallery)
    db.session.commit()
    flash('Gallery Deleted', 'blue')
    return redirect(url_for('.gallery_list'))

@bp.route('/messages')
@bp.route('/messages/<int:page>')
@login_required
def message_list(page=1):
    messages = Message.query.paginate(page, PER_PAGE, False)
    return render_template('dashboard/message/list.html', messages=messages.items)

@bp.route('/messages/new', defaults={'uid':None}, methods=['GET', 'POST'])
@bp.route('/messages/edit/<uid>', methods=['GET', 'POST'])
@login_required
def message_action(uid):

    message = Message.query.filter_by(uid=uid).first() 
    message.read = True
    db.session.commit()
    #form = MessageForm(obj=message)

    #if form.validate_on_submit():
       
   #     if uid is None:
    #        message_to_add = Gallery(name=form.name.data, email=form.email.data, text=form.text.data)
    #        db.session.add(message_to_add)
   #         flash('Message  created successfully', 'blue')
   #     else:
   #         message.name = form.name.data
   #         message.email = form.email.data
   #         message.text = form.text.data
   #         flash('Message updated successfully', 'blue')
   #     db.session.commit()
   #     return redirect(url_for('.message_list'))
    return render_template('dashboard/message/form.html', form=form, message=message)

@bp.route('/messages/delete/<uid>', methods=['GET', 'POST'])
@login_required
def message_delete(uid):
    message = Messgae.query.filter_by(uid=uid).first()
    db.session.delete(message)
    db.session.commit()
    flash('Message Deleted', 'blue')
    return redirect(url_for('.message_list'))

