#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2023/5/17
# CreatTIME : 16:23
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
# 导入项目view
# from apps import user,test
# from apps.user import user, menu
# from apps import test
from apps.route import *
from server_core.middleware import register_cors, register_exception
from server_core.conf import conf


def createapp():
    app = FastAPI(
        title=conf.title,
        description=conf.description,
        version=conf.VERSION,
    )
    # app.mount('/static', StaticFiles(directory='apps/static'), name='static')

    # 用户相关
    # app.include_router(user.route, tags=["用户"])
    # app.include_router(menu.route, tags=["菜单"])
    # app.include_router(test.route, tags=["测试"])
    app.include_router(users.route, tags=["redis测试"])

    # @app.get("/")
    # def home():
    #     return RedirectResponse(url="/otdisk/index.html")

    @app.get("/test")
    def test():
        return {"holy": "shit！"}

    register_cors(app)  # 跨域设置
    # register_exception(app)

    return app
