from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 为app指定数据库，并设置配置信息
app.config['SQLALCHEMY_DATABASE_URI']=\
'mysql://root:123456@localhost:3306/myflask'
# 指定执行完成后，自动提交申请
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),nullable=False,unique=True)
    password = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(50))
    url = db.Column(db.String(80))
    # source_url = db.Column(db.String(80))
    # 创建与作品集的反向引用
    works = db.relationship('Works',backref='user',lazy='dynamic')

    def __init__(self,username,password,email=None,url=None):
        self.username = username
        self.password = password
        self.email = email
        self.url = url
        # self.source_url = source_url

    def __repr__(self):
        return "<users:%r>" % self.username

class Works(db.Model):
    __tablename__ = 'works'
    id = db.Column(db.Integer,primary_key=True)
    products = db.Column(db.String(30))
    # 创建与用户名的关联属性
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __init__(self,product):
        self.products = product

    def __repr__(self):
        return "<works:%r>"%self.products


def dbs_create():
    # 将创建好的实体类映射到数据库
    db.create_all()

def dbs_drop():
    # 将创建好的实体类映射到数据库
    db.drop_all()
