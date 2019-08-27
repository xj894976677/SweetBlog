from flask import Flask
# 从config导入Config类，配置app
from config import Config
# 导入SQLAlchemy 操作数据库
from flask_sqlalchemy import SQLAlchemy
# 导入Migrate 为了数据库迁移
from flask_migrate import Migrate
# 导入LoginManager 管理用户登陆状态
from flask_login import LoginManager


# 创建app实例
app = Flask(__name__)
# 通过config类配置app
app.config.from_object(Config)
# 创建SQLAlchemy实例db,并绑定app
db = SQLAlchemy(app)
# 创建迁移引擎对象
migrate = Migrate(app, db)
# 创建Flask_login 初始化
login = LoginManager(app)
# 绑定需要处理登陆的视图函数名为login
login.login_view = 'login'

# 引入路由文件与数据库模型类，放在最后防止与其文件循环引用
from app import routes, models
