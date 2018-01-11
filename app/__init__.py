#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from flask import Flask
import redis
from flask_session import Session
from auth.auth import Auth

from .views.login import account
# from .views.user import user
from .views.main import main


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = "secret_key"
    # 设置配置文件
    app.config['SESSION_TYPE'] = 'redis'
    # 注册蓝图
    app.register_blueprint(account)
    # app.register_blueprint(user)
    app.register_blueprint(main)
    #
    # @app.before_request
    # def check_login():
    #     print('定义验证方法')

    # 注册组件
    # 为Flask-session组件提供的配置
    app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
    app.config['SESSION_REDIS'] = redis.Redis(host='47.93.252.50', port='6379', password='Yfga0310')  # 用于连接redis的配置
    app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
    app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
    app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上 session:cookie值进行加密
    Session(app)


    #Auth验证
    Auth(app)


    return app
