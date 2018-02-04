#!/usr/bin/env python 
#-*-coding:utf-8-*-

'''
通过DOM来处理xml

           根节点
    元素节点   属性节点

元素节点    元素节点     元素节点
文本节点            文本节点

Document接口来表示xml文档，
parse-->输入参数是文件或者文件对象
parentNode-->获取父节点
childNode-->获取子节点集合
firstChild&lastChild-->获取第一个节点和最后一个节点

Element-->实现对元素节点的操作

'''



import xml.dom.minidom
import  os

#获取docment的对象
dom=xml.dom.minidom.parse(os.path.join(os.path.dirname(__file__),'data','system.xml'))

db=dom.documentElement
#查询节点
name=db.getElementsByTagName('url')
print name[0].firstChild.data












# import  xml.dom.minidom
#
# dom=xml.dom.minidom.parse('D:/git/Python/sanUI/data/system.xml')
# db=dom.documentElement
# name=db.getElementsByTagName('url')
# nameValue=name[0]
# print nameValue
# print nameValue.firstChild

