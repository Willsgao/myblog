from flask import render_template,redirect,request,session

from . import release
from ..models import *

@release.route('/release',methods=['GET','POST'])
def release_views():
    if request.method == 'GET':
        if 'uid' in session and 'uname' in session:
            user = User.query.filter_by(id=session['uid'],\
                uname=session['uname']).first()
            blogtypes = BlogType.query.all()
            categories = Category.query.all()
            print(categories)
            if user.is_author:
                return render_template('release.html',params=locals())
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        tilte = request.form.get('author')
        blogtype = request.form.get('list')
        category = request.form.get('category')
        editor = request.form.get('article')
        content = request.form.get('content')
        print(tilte,blogtype,category,editor,content)
        return '%s'%content


