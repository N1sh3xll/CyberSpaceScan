# -*- coding: utf-8 -*-
"""
@Time   ： 2022/3/31 15:50
@Author ： hem1ock
@File   :  user.py

"""

from flask import Blueprint, request
import json

userbp = Blueprint("user", __name__, url_prefix="/api/user/")


@userbp.route("login", methods=['POST'])
def login():
    data = request.get_data()  # 获取post请求body数据
    # print(data)
    js_data = json.loads(data)  # 将字符串转成json
    # print(js_data)
    # 验证如果是admin用户名，即登录成功，返回admin的token，否则验证失败
    if "username" in js_data and js_data['username'] == 'admin' and js_data['password'] == 'admin':
        result_success = {"code": 20000, "data": {"token": "admin-token"}}
        return result_success
    else:
        result_error = {"code": 60204, "message": "账号或密码错误,请重新输入!!!"}
        return result_error


@userbp.route("info", methods=['GET'])
def info():
    # 获取GET中请求token参数值
    token = request.args.get('token')
    if token == 'admin-token':
        result_success = {
            "code": 20000,
            "data": {
                "roles": ["admin"],
                "introduction": "I am a super administrator",
                # "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                "avatar": "https://s2.loli.net/2022/03/29/93dIKSETJZCWmOk.png",
                "name": "Super Admin"}
            }
        return result_success
    else:
        result_error = {"code": 60204, "message": "用户信息获取错误"}
        return result_error


@userbp.route("logout", methods=['POST'])
def logout():
    request.get_data()
    return {
        "code": 20000,
        "data": 'success'
    }
