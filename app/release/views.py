from flask import render_template,redirect,request,session

from . import release
from ..models import *

@release.route('/release',methods=['GET','POST'])
def release_views():
    if request.method == 'GET':
        if 'uid' in session and 'uname' in session:
            user = User.query.filter_by(id=session['uid'],\
                uname=session['uname']).first()
            if user.is_author:
                return render_template('release.html')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        pass
