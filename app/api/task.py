# -*- coding: utf-8 -*-
"""
@Time   ： 2022/4/6 20:49
@Author ： hem1ock
@File   :  task.py

"""
import logging
from flask import Blueprint, request
import json

from config import resp, logging
from config.logging import logger
from mysql.conn import *

taskbp = Blueprint("task", __name__, url_prefix="/api/task/")


@taskbp.route("new", methods=['POST'])
def newtask():
    data = request.get_data()  # 获取post请求body数据

    js_data = json.loads(data)  # 将字符串转成json
    logger.info("[-] 提交的表单内容%s " % js_data)

    # 初始化数据库链接
    connection = connectDB().connection()
    # 定义默认返回结构体
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": [],
    }
    # with connection:
    # 先做个查询，判断keyCode是否重复（这里的关键词最初定义为唯一项目编号或者为服务的应用名）
    with connection.cursor() as conn:
        select = "SELECT * FROM `task` WHERE `task_name`=%s"
        conn.execute(select, (js_data["name"],))
        print(js_data["name"])
        result = conn.fetchall()
    if len(result) > 0:
        resp_data["code"] = 20001
        logger.error("[-] 任务名称 %s 已存在" % js_data["name"])
        resp_data["message"] = "任务名称已存在!!!请重新输入!!!"
        return resp_data

    with connection.cursor() as cursor:
        # 拼接插入语句,并用参数化%s构造防止基本的SQL注入
        # 其中id为自增，插入数据默认数据设置的当前时间
        logger.info("[+] 添加task表数据")
        sql = "INSERT INTO `task` (`task_name`,`task_target`,`task_port`,`task_poc`,`task_option`) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (js_data["name"], js_data["target"], js_data["port"], js_data["vul"], js_data["type"]))
        # 提交执行保存插入数据
        connection.commit()
        logger.info("[-] 添加任务数据%s 到task表成功" % js_data["name"])
        return resp_data


@taskbp.route("get", methods=['POST'])
def gettask():
    get_data = request.get_data()  # 获取post请求body数据
    body = json.loads(get_data)  # 将字符串转成json
    logger.info("[-] 提交的表单内容%s " % body)
    print(body)
    # 基础语句定义
    sql = ""
    # 初始化数据库链接
    connection = connectDB().connection()
    # 定义默认返回结构体
    pageSize = 10 if body['pageSize'] is None else body['pageSize']
    currentPage = 1 if body['currentPage'] is None else body['currentPage']

    sql = sql + ' ORDER BY `task_id` ASC LIMIT {},{}'.format((currentPage - 1) * pageSize, pageSize)
    print(sql)

    with connection:
        with connection.cursor() as cursor:
            sql2 = 'SELECT * FROM `task` ' + sql
            sql3 = 'SELECT COUNT(*) as `count` FROM (' + sql2 + ') temp'
            print("sql2:" + sql2)
            print("sql3:" + sql3)
            cursor.execute('SELECT COUNT(*) as `count` FROM `task`')
            total = cursor.fetchall()
            cursor.execute(sql3)
            print(total)
        # 执行查询
        with connection.cursor() as cursor:
            # 拼接插入语句,并用参数化%s构造防止基本的SQL注入
            # 其中id为自增，插入数据默认数据设置的当前时间
            logger.info("[+] 查询task表数据")
            sql = "select * FROM `task`" + sql
            cursor.execute(sql)
            data = cursor.fetchall()
    # 按返回模版格式进行json结果返回
    response = resp.resp_format_success
    response['data'] = data

    print(total[0]['count'])
    response['total'] = total[0]['count']
    return response
@taskbp.route("delete", methods=['DELETE'])
def task_delete():
    # 返回的reponse
    resp_data = {
        "code": 20000,
        "message": "success",
        "data": []
    }
    # 方式1：通过params 获取id
    ID = request.args.get('task_id')
    # 做个参数必填校验
    if ID is None:
        resp_data["code"] = 20002
        resp_data["message"] = "请求id参数为空"
        return resp_data
    # 初始化数据库链接
    connection = connectDB().connection()
    # 定义默认返回结构体
    with connection.cursor() as cursor:
        sql = "DELETE from `task` where task_id=%s"
        cursor.execute(sql, ID)
        connection.commit()
    return resp_data