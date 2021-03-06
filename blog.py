from app import create_app, db, cli
from app.models import User, Post

# 配置flask上下文  让程序flask run之后可以执行flask shell中调用返回的字典中的数据
app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)
