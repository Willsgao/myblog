from flask import render_template,redirect,request,session

from . import main
from ..models import *

@main.route('/')
def index_views():
    categories = Category.query.all()
    if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id=session['uid'],\
            uname=session['uname']).first()
    topics = Topic.query.order_by('id desc').all()
    print(topics)
    return render_template('index.html',params=locals())

@main.route('/register',methods=['GET','POST'])
def register_views():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        loginname = request.form.get('loginname')
        uname = request.form.get('username')
        email = request.form.get('email')
        url = request.form.get('url')
        upwd = request.form.get('password')
        try:
            user = User(loginname,uname,email,upwd,url)
            print("++++++++++++++")
            print(user)
            db.session.add(user)
            return redirect('/login')
        except Exception as e:
            print('**************')
            print(e)
            return render_template('register.html')

@main.route('/login',methods=['GET','POST'])
def login_views():
    if request.method == 'GET':
        if 'uid' in session and 'uname' in session:
            return redirect('/')
        else:
            return render_template('login.html')
    else:
        loginname = request.form.get('username')
        upwd = request.form.get('password')
        user = User.query.filter_by(loginname=loginname,upwd=upwd).first()
        if user:
            session['uid'] = user.id
            session['uname'] = user.uname
            return redirect('/')
        else:
            errMsg = '用户名或密码有误，请重新输入！'
            return render_template('login.html',errMsg=errMsg)

@main.route('/logout')
def logout_views():
    if 'uid' in session and 'uname' in session:
        del session['uid']
        del session['uname']  
        return redirect('/')
    else:
        return redirect('/login')

@main.route('/info')
def info_views():
    # 查询所有的Category信息
    categories = Category.query.all()
    topics = Topic.query.all()
    # 获取登录信息
    if 'uid' in session and 'uname' in session:
    # if session['uid'] and session['uname']:
        user = User.query.filter_by(id=session.get('uid')).first()
        print(user)
    tid = request.args.get('id')
    print(tid)
    topic = Topic.query.filter_by(id=tid).first()
    return render_template('info.html',params=locals())
