from flask import Flask, render_template,request,redirect
from models import Users,Works,dbs_create,dbs_drop,app,db
from flask_sqlalchemy import SQLAlchemy 
import pymysql
pymysql.install_as_MySQLdb()


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

# # 创建数据库
# @app.route('/createdbs')
# def createdbs_views():
#     dbs_create()
#     print('创建成功！')
#     return '数据库创建成功！'

# # 删除数据库
# @app.route('/dropdbs')
# def dropdbs_views():
#     dbs_drop()
#     print('创建成功！')
#     return '数据库删除成功！'

@app.route('/list')
@app.route('/list.html')
def list_views():
    return render_template('list.html')

@app.route('/register',methods=['GET','POST'])
@app.route('/register.html',methods=['GET','POST'])
def register_views():
    if request.method == 'GET':
        refurl = request.headers.get('Referer','')
        return render_template('register.html', refurl=refurl)
    else:
        # 获取注册基本信息
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        url = request.form.get('url')
        # 获取来源地址
        source_url = request.form.get('source_url')
        # 执行注册用户信息插入数据库操作
        users = Users(username,password,email,url)
        db.session.add(users)
        print('插入成功！')

        global SOURSE_url0
        SOURSE_url0 = source_url
        print('SOURSE_url0=',SOURSE_url0)

        return redirect('/login')

@app.route('/login',methods=['GET','POST'])
@app.route('/login.html',methods=['GET','POST'])
def login_views():
    if request.method == 'GET':
        source_url = request.headers.get('Referer','')
        print('source_url=',source_url)

        global SOURSE_url1 
        SOURSE_url1 = source_url
        print('SOURSE_url1=',SOURSE_url1)
        return render_template('login.html', source_url=source_url)
    else:
        print('source_url1=',SOURSE_url1)
        username = request.form.get('username')
        password = request.form.get('password')
        source_url = request.form.get('source_url')
        if SOURSE_url1.split('/')[-1] == 'register.html':
            return redirect(SOURSE_url0)
        else:
            return redirect(SOURSE_url1)

@app.route('/photo.html')
def photo_views():
    return render_template('photo.html')

@app.route('/time.html')
def tome_views():
    return render_template('time.html')

@app.route('/gbook.html')
def gbook_views():
    return render_template('gbook.html')

@app.route('/about.html')
def about_views():
    return render_template('about.html')

@app.route('/release.html')
def release_views():
    return render_template('release.html')


if __name__ == "__main__":
    app.run(debug=True,port=5556)
