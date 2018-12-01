from flask import render_template,session

from . import gbook
from ..models import *


@gbook.route('/gbook')
def gbook_index():
    if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id=session['uid'],\
            uname=session['uname']).first()
    return render_template('gbook.html',params=locals())