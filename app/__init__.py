from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # 配置app
    app.config['DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI']=\
    'mysql://root:123456@localhost:3306/myblog'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']='zixinrenshengerbainian'

    # 使用app初始化db
    db.init_app(app)

    # 使用bluprint关联程序
    # 关联main程序
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 关联main程序
    from .lists import lists as lists_blueprint
    app.register_blueprint(lists_blueprint)

    # 关联release程序
    from .release import release as release_blueprint
    app.register_blueprint(release_blueprint)

    # 关联photos程序
    from .photos import photos as photos_blueprint
    app.register_blueprint(photos_blueprint)

    # 关联time程序
    from .time import time as time_blueprint
    app.register_blueprint(time_blueprint)

    #　关联gbook程序
    from .gbook import gbook as gbook_blueprint
    app.register_blueprint(gbook_blueprint)

    # 关联about程序
    from .about import about as about_blueprint
    app.register_blueprint(about_blueprint)


    return app    

