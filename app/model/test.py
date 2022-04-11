# -*- coding: utf-8 -*-
"""
@Time   ： 2022/3/28 23:19
@Author ： hem1ock
@File   :  test.py

"""
# import json
#
# import requests
from model.POC.inc.init import *
from model.POC.inc.output import show
import os

if __name__ == '__main__':

    data = {'username': 'admin', 'password': 123456}
    # data1 = json.dumps(data)
    # print(type(data)) #<class 'dict'>
    # print(type(data1)) # <class 'str'>
    # data2 = json.loads(data1)
    # print(data2)  #{'username': 'admin', 'password': 123456}
    # print(type(data2)) # <class 'dict'>

    # poc_modole_list = get_poc_modole_list()
    # show(poc_modole_list)

    # command = 'python POC\pocbomber.py --show'
    # os.system(command)
