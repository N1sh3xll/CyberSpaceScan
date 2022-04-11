# -*- coding: utf-8 -*-
"""
@Time   ： 2022/3/31 21:38
@Author ： hem1ock
@File   :  conn.py

"""

import pymysql.cursors
from dbutils.pooled_db import PooledDB

# from flask_sqlalchemy import SQLAlchemy


# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'cyberspace'
USERNAME = 'root'
PASSWORD = '123456'


def connectDB():
    # PyMySQL使用文档  https://pymysql.readthedocs.io
    # connection = pymysql.connect(host='localhost',  # 数据库IP地址或链接域名
    #                              user='root',  # 设置的具有增改查权限的用户
    #                              password='123456',  # 用户对应的密码
    #                              database='cyberspace',  # 数据表
    #                              charset='utf8',  # 字符编码
    #                              cursorclass=pymysql.cursors.DictCursor)  # 结果作为字典返回游标
    # 初始化数据库连接，使用pymysql连接，
    # 第一参数为 creator 指定那种连接模式 mincached ：启动时开启的空的连接数量
    # maxcached ：连接池最大可用连接数量 maxshared : 连接池最大可用共享连接数量
    # maxconnections : 最大允许连接数量maxusage ：单个丽娜姐最大复用次数 blocking ：达到最大数量时是否阻塞
    pool = PooledDB(pymysql, mincached=2, maxcached=5, host=HOSTNAME, port=PORT,
                    user=USERNAME, passwd=PASSWORD, database=DATABASE,
                    cursorclass=pymysql.cursors.DictCursor)
    return pool


# # 或者通过with方式
# with pool.connection() as db:
#   with db.cursor as cur:
#        cur.execute(...)
#        res = cur.fetchone()


