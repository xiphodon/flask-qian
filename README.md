# flask-qian
<hr>

## python -m venv venv
初始化项目初始环境python -m venv venv(环境文件名)

## requirements.txt
生成requirements.txt文件

    pip freeze > requirements.txt
    
安装requirements.txt依赖

    pip install -r requirements.txt

## Flask==1.0.2:
###flask web 框架

临时环境变量
    set FLASK_APP=qff
    set FLASK_ENV=development

运行
    flask run

shell 调试
    flask shell


## Flask-Migrate==2.5.0:
###flask 数据模型迁移插件

初始化文件（只需要执行一次）

    flask db init

通过引用的数据模型更新到init生成的migrations文件中

    flask db migrate --message '日志信息'

更新数据模型到数据库

    flask db upgrade

退回数据库

    flask db downgrade


## Flask-SQLAlchemy==2.4.0:
###orm 映射插件

	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


## Flask-Session==0.3.1:
###flask session 插件

可以持久化session到数据库
各个数据库均可配置

    app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
    # app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
    # app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
    # app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
    # app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='123123')  # 用于连接redis的配置


## Bootstrap-Flask==1.0.10:
###flask bootstrap 插件


## Flask-DebugToolbar==0.10.1:
###flask 调试工具条


## mysql-connector-python==8.0.16:
###mysql 驱动
mysqlconnector替换pymysql，连接mysql 对中文支持更好

## Flask-Cache==0.13.1:
###flask 缓存

