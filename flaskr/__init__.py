import os
from flask import Flask


# 应用工厂函数
def create_app(test_config=None):
    # 创建 flask 实例
    app = Flask(__name__, instance_relative_config=True)
    # 设置应用的缺省配置
    app.config.from_mapping(
        SECRET_KEY='dev',  # 保证数据安全性，生产环境应该使用随机值
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),  # 数据库文件存放路径
    )

    if test_config is None:
        # 使用配置文件
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)  # 创建实例文件夹
    except OSError:
        pass

    # 路由
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    # 注册认证蓝图
    from . import auth
    app.register_blueprint(auth.bp)

    # 注册博客蓝图
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


    return app


