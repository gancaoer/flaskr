import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

'''连接 SQLite 数据库'''


def get_db():
    # g 特殊对象，独立于每一个请求，可以储存可能多个函数都会用到的数据，
    # 把数据库连接储存于其中，可以多次使用，而不用在同一个请求中每次调用get_db时都创建一个新的连接。
    if 'db' not in g:
        # 建立一个数据库连接
        g.db = sqlite3.connect(
            # current_app 该对象指向处理请求的Flask应用。当应用创建后，在处理一个请求时， get_db会被调用。这样就需要使用current_app
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    # 打开一个数据库文件并执行
    with current_app.open_resource('schema.sql') as f:
        # 执行多条sql语句
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    # 在返回响应后进行清理时调用此函数
    app.teardown_appcontext(close_db)

    # 添加一个新的可与flask一起工作的命令
    app.cli.add_command(init_db_command)