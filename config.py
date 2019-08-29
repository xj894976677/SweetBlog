import os
basedir = os.path.dirname(__file__)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    # 配置sqlite数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///'+os.path.join(basedir, 'database.sqlite')
    # 配置不需要flask-SQLALCHEMY的该特征，即追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['your-email@example.com']
    POSTS_PER_PAGE = 3
