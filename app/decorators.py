# third party imports
from functools import wraps
from flask_login import current_user
from flask import url_for, redirect, flash

def access_required(access_level):
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
                    
            if not current_user.is_allowed(access_level):
                
                flash('You do not have permission to view this page')
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)
        return decorator_function
    return decorator    

