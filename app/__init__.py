import logging
from logging.handlers import RotatingFileHandler
import os


from flask import Flask, request
# 从config导入Config类，配置app
from config import Config
# 导入SQLAlchemy 操作数据库
from flask_sqlalchemy import SQLAlchemy
# 导入Migrate 为了数据库迁移
from flask_migrate import Migrate
# 导入LoginManager 管理用户登陆状态
from flask_login import LoginManager
# 导入mail
from flask_mail import Mail
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from flask import current_app


# 创建SQLAlchemy实例db,并绑定app
db = SQLAlchemy()
# 创建迁移引擎对象
migrate = Migrate()
# 创建Flask_login 初始化
login = LoginManager()
# 绑定需要处理登陆的视图函数名为login
login.login_view = 'auth.login'
# 绑定Mail
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')
    return app

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])


# 引入路由文件与数据库模型类，放在最后防止与其文件循环引用
from app import models
