from flask import render_template,redirect,request,session

from . import lists
from ..models import *

@lists.route('/list')
def list_views():
    categories = Category.query.all()
    if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id=session['uid'],\
            uname=session['uname']).first()
        print(user)
    id = request.args.get('id')
    topics = Topic.query.filter_by(category_id=id).order_by('id desc').all()
    print(topics)
    return render_template('list.html',params=locals())
    
