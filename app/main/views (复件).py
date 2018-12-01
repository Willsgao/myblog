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

@main.route('/info',methods=['GET','POST'])
def info_views():
    if request.method == 'GET':
        # 查询所有的Category信息
        categories = Category.query.all()
        topics = Topic.query.all()

        # 查询具体的文章
        tid = request.args.get('id')
        if tid:
            # print(tid)
            topic = Topic.query.filter_by(id=tid).first()
            topic.read_num = int(topic.read_num)+1
            db.session.add(topic)
            prevtopic = Topic.query.filter(Topic.id<tid).order_by('id desc').first()
            nexttopic = Topic.query.filter(Topic.id>tid).first()
        if 'uid' in session and 'uname' in session:
        # if session['uid'] and session['uname']:
            user = User.query.filter_by(id=session.get('uid')).first()
            user_id = session.get('uid')
        return render_template('info.html', params=locals())

@main.route('/info_ajax')
def info_ajax_views():
        # 获取登录信息
        user_id = ''
        if 'uid' in session and 'uname' in session:
        # if session['uid'] and session['uname']:
            user = User.query.filter_by(id=session.get('uid')).first()
            user_id = session.get('uid')

        # 获取Ajax请求
        topic_id = request.args.get('topic_id')
        like = request.args.get('like')
        # if like == 1:
        topic = Topic.query.filter_by(id=topic_id).first()
        voke = topic.voke_users.filter_by(user_id=user_id).first()
        if voke:
            dic = {
                'status':1,
                'msg':'已经点过赞'
            }
        else:
            user = User.query.filter_by(id=user_id).first()
            # 增加多对多外键关联关系
            topic.voke_users.append(user)
            db.session.add(topic)
            dic = {
                'status':0,
                'msg':'点赞成功'
            }
        data = json.dumps(dic)

        return render_template('info.html', params=locals())

