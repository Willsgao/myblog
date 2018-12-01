#! /usr/bin/env python3
from app import create_app,db
from app.models import Category,BlogType,Topic,User,Reply,Voke
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db,Category=Category, 
        BlogType=BlogType,Topic=Topic,User=User,
        Reply=Reply,Voke=Voke)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    app.run(host='0.0.0.0')




server {
    listen  8000;
    server_name  fruitday.abc;
    charset  utf-8;
    client_max_body_size 75M;
    location /static{
    alias /home/tarena/githubs/fruitshop/static;
}
    location/ {
      include uwsgi_params;
      uwsgi_pass 127.0.0.1:8002;
      #include /home/tarena/githubs/fruitshop/uwsgi_params;
}

}



server {
    listen  8000;
    server_name  fruitday.abc;
    charset  utf-8;
    client_max_body_size  75M;
    location /static {
    alias /home/tarena/githubs/fruitshop/static;
}
    location / {
      include uwsgi_params;
      uwsgi_pass 127.0.0.1:8002;
      #include /home/tarena/githubs/fruitshop/uwsgi_params;
}
}
