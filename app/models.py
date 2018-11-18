from . import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    cate_name = db.Column(db.String(50),nullable=False)
    # 反向引用Topic数据表
    topics = db.relationship('Topic',backref='category',lazy='dynamic')

    def __init__(self,cate_name):
        self.cate_name = cate_name

class BlogType(db.Model):
    __tablename__ = 'blogtype'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    type_name = db.Column(db.String(20),nullable=False)
    # 反向引用Topic数据表
    topics = db.relationship('Topic',backref='blogtype',lazy='dynamic')

    def __init__(self,type_name):
        self.type_name = type_name

class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    title = db.Column(db.String(200),nullable=False)
    pub_date = db.Column(db.DateTime,nullable=False)
    read_num = db.Column(db.Integer)
    content = db.Column(db.Text,nullable=False)
    images = db.Column(db.Text)
    blogtype_id = db.Column(db.Integer,db.ForeignKey('blogtype.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    replies = db.relationship('Reply',backref='topic',lazy='dynamic')
    voke_users = db.relationship(
        'User',
        secondary='voke',
        lazy='dynamic',
        backref=db.backref('voke_users',lazy='dynamic')
        )


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    loginname = db.Column(db.String(50),nullable=False)
    uname = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200))
    upwd = db.Column(db.String(30),nullable=False)
    is_author = db.Column(db.SmallInteger,default=0)
    topics = db.relationship('Topic',backref='user',lazy='dynamic')
    replies = db.relationship('Reply',backref='user',lazy='dynamic')
    voke_topics = db.relationship(
        'Topic',
        secondary='voke',
        lazy='dynamic',
        backref=db.backref('voke_topics',lazy='dynamic')
        )

    def __init__(self,loginname,uname,email,upwd,url=None):
        self.loginname = loginname
        self.uname = uname 
        self.email = email
        self.url = url
        self.upwd = upwd

    def __repr__(self):
        return "<User:%r>"%self.loginname

class Reply(db.Model):
    __tablename__ = 'reply'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    content = db.Column(db.Text,nullable=False)
    reply_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))

# 使用db.Table创建第三张关联表
Voke = db.Table(
    # 第三张关联表名称
    'voke',
    # 指定关联表主键
    db.Column('id',db.Integer,primary_key=True),
    # 指定关联表外键
    db.Column('topic_id',db.Integer,db.ForeignKey('topic.id')),
    db.Column('user_id',db.Integer,db.ForeignKey('user.id'))
    )





