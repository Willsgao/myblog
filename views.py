from flask import render_template,redirect,request,session

from . import main
import json
from ..models import *
from datetime import datetime

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
    if request.method == 'POST':
        # user_id = session['uid']
        topic_id = request.args.get('id','')
        html = request.form.get('content')
        print('html=',html)
        return redirect('/info')
    else:
        # 查询所有的Category信息
        categories = Category.query.all()
        topics = Topic.query.all()

        # # 获取登录信息
        # if 'uid' in session and 'uname' in session:
        user = User.query.filter_by(id=session.get('uid','')).first()
        user_id = session['uid']
        tid = request.args.get('id','')
        like = request.args.get('like','')
        print('likel',like,'likel')
        topic_id = tid
        print('88888888888888888')
        print(topic_id)
        print(user_id)
        print(tid)
        print('88888888888888888')
        if tid:
            print(tid)
            topic = Topic.query.filter_by(id=tid).first()
            replies = Reply.query.filter_by(topic_id=tid).all()

            print('replies已经生成')
            topic.read_num = int(topic.read_num)+1
            db.session.add(topic)
            prevtopic = Topic.query.filter(Topic.id<tid).order_by('id desc').first()
            nexttopic = Topic.query.filter(Topic.id>tid).first()
            if user_id and like:
                topic = Topic.query.filter_by(id=topic_id).first()
                user = User.query.filter_by(id=user_id).first()
                print('+++++++++++++++++++++++++++++++')
                voke = topic.voke_users.filter_by(id=user_id).first()
                print(type(topic.voke_users))
                print('+++++++++++++++++++++++++++++++')
                if voke:
                    zans = topic.voke_users.count()
                    # dic = {
                    #     'status':1,
                    #     'msg':'您已赞过！',
                    #     'zans':zans
                    # }
                else:
                    # 增加多对多外键关联关系
                    topic.voke_users.append(user)
                    db.session.add(topic)
                    zans = topic.voke_topics.count()
                #     dic = {
                #         'status':0,
                #         'msg':'点赞成功！',
                #         'zans':zans
                #     }            
                # dicstr = json.dumps(dic)
                print(dicstr)

        return render_template('info.html',params=locals())

# @main.route('/topic_zans')
# def topic_zans():
#     topic_id = request.args.get('id','')
#     user_id = session['uid']
#     like = request.args.get('like','')
#     print('777777777777777777777777')
#     print(topic_id)
#     print(user_id)
#     print('88888888888888888')
#     if user_id and like:
#         topic = Topic.query.filter_by(id=topic_id).first()
#         user = User.query.filter_by(id=user_id).first()
#         print('+++++++++++++++++++++++++++++++')
#         voke = topic.voke_users.filter_by(id=user_id).first()
#         print(type(topic.voke_users))
#         print('+++++++++++++++++++++++++++++++')
#         if voke:
#             zans = topic.voke_users.count()
#             dic = {
#                 'status':1,
#                 'msg':'您已赞过！',
#                 'zans':zans
#             }
#         else:
#             # 增加多对多外键关联关系
#             topic.voke_users.append(user)
#             db.session.add(topic)
#             zans = topic.voke_topics.count()
#             dic = {
#                 'status':0,
#                 'msg':'点赞成功！',
#                 'zans':zans
#             }            
#         dicstr = json.dumps(dic)
#         print(dicstr)
#     else:
#         pass
#     return json.dumps(dic)

