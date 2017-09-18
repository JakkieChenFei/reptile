__author__ = 'JakkieChenFei'
from urllib import request
import re
import sys
import importlib
import os

#工具类
class TOOL:
    removeAddr = re.compile('')
#知乎爬虫C:\Users\jiaxie\AppData\Local\Programs\Python\Python36-32\Scripts\
class ZHIHU:
    #初始化，传入基地址
    def __init__(self, baseUrl):
        #基地址
        self.baseURL = baseUrl
        #工具类
        self.Tool = TOOL()
        #写入文件地址
        self.file = ''
        self.html = ''
    def test(self):
        print(self.baseURL)
    def getHtml(self):
        page = request.urlopen(self.baseURL)
        self.html = page.read()
    def getImg(self):
        #self.getHtml()
        self.html = self.html.decode('utf-8')
        reg = r'src="(.+?\.jpg)"'
        imgre = re.compile(reg)
        imglist = re.findall(imgre, self.html)
        x = 0
        for imgurl in imglist:
            self.file = '..\source\images\%s.jpg' % x
            request.urlretrieve(imgurl, self.file)
            x += 1

#address = input("input your zhihu address:\n")
zhiHu = ZHIHU('')
zhiHu.getHtml()
zhiHu.getImg()

