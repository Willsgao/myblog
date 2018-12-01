from flask import render_template,session

from . import time
from ..models import *


@time.route('/time')
def time_index():
    if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id=session['uid'],\
            uname=session['uname']).first()
    return render_template('time.html',params=locals())