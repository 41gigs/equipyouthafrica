# third party imports
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
# local imports
from ..extensions import db
from ..forms import LoginForm, JoinForm
from ..models import User, Setting

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():

    landing_image_2 = None
    landing_image_2_setting = Setting.query.filter_by(key='LANDING_IMAGE_2').first()
    if landing_image_2_setting.image:
        landing_image_2  = landing_image_2_setting.imgsrc


    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() 

        if user is not None and user.check_password(form.password.data): 
            login_user(user, form.remember_me.data)    
            flash('You are logged in', 'blue')   
            return redirect(request.args.get('next') or url_for('dashboard.root'))  
        flash('Invaild Credienials or Password', 'red')   

    form.email.data = ''   
    form.password.data= ''
    return render_template('auth/login.html', form=form, landing_image_2=landing_image_2)

#@bp.route('/join', methods=['GET', 'POST'])
#def join():
#    form = JoinForm()
#    if form.validate_on_submit():
#        user = User(email=form.email.data, password=form.password.data, name=form.name.data)
#        db.session.add(user)
#        db.session.commit()
#        flash('User Added', 'is-info')
#        return redirect(url_for('.login'))
#    return render_template('auth/join.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out', 'blue')
    return redirect(url_for('index.root'))
