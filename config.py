import os

basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前.py文件的绝对路径

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'blog.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    # 配置sqlite数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///'+os.path.join(basedir, 'database.sqlite')
    # 配置不需要flask-SQLALCHEMY的该特征，即追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['xj894976677@163.com']
    POSTS_PER_PAGE = 3
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    LANGUAGES = ['en', 'zh']
