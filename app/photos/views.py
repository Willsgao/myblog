from flask import render_template,session

from . import photos
from  ..models import *

@photos.route('/photos')
def photos_index():
    if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id=session['uid'],\
            uname=session['uname']).first()
    return render_template('photos.html',params=locals())