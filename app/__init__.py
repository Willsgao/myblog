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


    return app    

# {overflow: 
#   hidden; margin-bottom: 20px; padding: 20px; background: FFF;\
#  -webkit-box-shadow: 0 2px 5px 0 rgba(146, 146, 146, .1);\
#  -moz-box-shadow: 0 2px 5px 0 rgba(146, 146, 146, .1);\
#   box-shadow: 0 2px 5px 0 rgba(146, 146, 146, .1); \
#   -webkit-transition: all 0.6s ease; -moz-transition: all 0.6s ease; \
#   -o-transition: all 0.6s ease; transition: all 0.6s ease; }

# {
#     white-space: nowrap; 
#     overflow: hidden;
#     display: -webkit-box;
#     text-overflow: ellipsis;
#     -webkit-line-clamp: 1;
#     display: -moz-box;
#     display:block;
#     -webkit-box-orient: vertical;
#     -moz-box-orient: vertical;
# }