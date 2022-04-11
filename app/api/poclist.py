# -*- coding: utf-8 -*-
"""
@Time   ： 2022/3/30 0:09
@Author ： hem1ock
@File   :  poclist.py

"""
import logging

from flask import Blueprint, request
import json

from config import resp
from mysql.conn import *

pocbp = Blueprint("poc", __name__, url_prefix="/api/poc/")


@pocbp.route("/", methods=['GET'])
def logout():
    request.get_data()
    return {
        "code": 20000,
        "data": 'success'
    }


@pocbp.route('list', methods=['POST'])
def poc_list():
    get_data = request.get_data()  # 获取post请求body数据
    body = json.loads(get_data)  # 将字符串转成json
    logging.info("[-] 提交的表单内容%s " % body)
    print(body)
    # 基础语句定义
    sql = ""

    pageSize = 10 if body['pageSize'] is None else body['pageSize']
    currentPage = 1 if body['currentPage'] is None else body['currentPage']

    # # 拼接查询条件
    # if 'productId' in body and body['productId'] != '':
    #     sql = sql + " AND `productId` = '{}'".format(body['productId'])
    # if 'appId' in body and body['appId'] != '':
    #     sql = sql + " AND `appId` LIKE '%{}%'".format(body['appId'])
    # if 'note' in body and body['note'] != '':
    #     sql = sql + " AND `note` LIKE '%{}%'".format(body['note'])
    # if 'tester' in body and body['tester'] != '':
    #     sql = sql + " AND `tester` LIKE '%{}%'".format(body['tester'])
    # if 'developer' in body and body['developer'] != '':
    #     sql = sql + " AND `developer` LIKE '%{}%'".format(body['developer'])
    # if 'producer' in body and body['producer'] != '':
    #     sql = sql + " AND `producer` LIKE '%{}%'".format(body['producer'])
    #
    # # 排序和页数拼接
    sql = sql +' ORDER BY `poc_id` ASC LIMIT {},{}'.format((currentPage - 1) * pageSize, pageSize)
    print(sql)

    # 使用连接池链接数据库
    connection = connectDB().connection()

    with connection:
        # 先查询总数
        with connection.cursor() as cursor:
            sql2 ='SELECT * FROM `poc` '+sql
            sql3 = 'SELECT COUNT(*) as `count` FROM ('+ sql2+') temp'
            print("sql2:"+sql2)
            print("sql3:"+sql3)
            cursor.execute('SELECT COUNT(*) as `count` FROM `poc`')
            total = cursor.fetchall()
            cursor.execute(sql3)
            print(total)
        # 执行查询
        with connection.cursor() as cursor:
            # 查询poc表-按更新时间新旧排序
            sql = "select * from poc"  + sql
            print("查询poc表"+sql)
            # 查询poc表-按更新时间新旧排序
            cursor.execute(sql)
            data = cursor.fetchall()
            # print(data)
    # 按返回模版格式进行json结果返回
    response = resp.resp_format_success
    response['data'] = data

    print(total[0]['count'])
    response['total'] = total[0]['count']
    return response
