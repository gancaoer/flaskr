1. 新建项目、配置虚拟环境

2. 使用git进行版本控制，编写 .gitignore 文件

3. 应用设置：应用工厂

4. 定义和操作数据库：SQLite
    （1）连接数据库
    （2）创建表
    （3）在应用中注册数据库操作函数
    （4）初始化数据库文件：flask init-db
        会有一个 flaskr.sqlite 文件出现在项目所在文件夹的 instance 文件夹中

5. 创建蓝图，编写视图、模板、静态文件

6. 开发模式下运行应用（windows）
    set FLASK_APP=flaskr
    set FLASK_ENV=development
    flask run

7. 测试
    在tests目录中编写单元测试代码并运行测试，使用pytest
    pip install pytest coverage

8. 使项目可安装化
    描述文件 setup.py 描述项目及其从属的文件
    说明文件 MANIFEST.in 说明这些文件有哪些
    在虚拟环境中安装项目：pip install -e .
    运行项目：flask run

9. 部署和安装
    安装wheel 库：pip install wheel
    构建发行文件：python setup.py bdist_wheel
        构建的文件为 dist/flaskr-1.0.0-py3-none-any.whl
    在其他机器上部署
        （1）创建新的虚拟环境
        （2）安装whl文件：pip install flaskr-1.0.0-py3-none-any.whl
        （3）创建数据库
            export FLASK_APP=flaskr
            flask init-db
        （4）配置秘钥
            python -c 'import os; print(os.urandom(16))'
            将生成的值配置到 venv/var/flaskr-instance/config.py文件中
                SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
        （5）运行产品服务器
            pip install waitress
            waitress-serve --call 'flaskr:create_app'

