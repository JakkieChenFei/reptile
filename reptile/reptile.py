__author__ = 'JakkieChenFei'
# -*- coding:utf-8 -*-
from urllib import request
import re
#工具类
class TOOL:
    removeAddr = re.compile()
#知乎爬虫
class ZHIHU:
    #初始化，传入基地址
    def __init__(self, baseUrl):
        #基地址
        self.baseURL = baseUrl
        #工具类
        self.Tool = TOOL()
        #写入文件地址
        self.file = ''
    def test(self):
        print(self.baseURL)

address = input("input your zhihu address:\n")
zhiHu = ZHIHU(address)
zhiHu.test()

