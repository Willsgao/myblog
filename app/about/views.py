from flask import render_template,session

from . import about
from ..models import *


@about.route('/about')
def about_index():
    if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id=session['uid'],\
            uname=session['uname']).first()
    return render_template('about.html',params=locals())