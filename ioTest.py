#!/usr/bin/env python 
#-*-coding:utf-8-*-


'''
1.首先打开文件
2.指定已什么样的模式操作文件:r(只读) w(读写) a+(读写，在之前基础上进行) b(二进制)
3.对进行根据指定的模式操作文件
4.关闭文件
'''

def write_one():
	f = open('san.log', 'w')
	f.write('hello world')
	f.close()

def write_two():
	'''w-->写入前，之前的内容会被清空再写入新的内容'''
	f = open('san.log', 'w')
	f.write('hello world')
	f.close()

def write_three():
	'''a+-->写入前，会保存文件之前的内容，再之前内容的基础上写新的内容'''
	f = open('san.log', 'a+')
	f.write('hello world')
	f.close()

def read_one():
	'''读取文件的所有内容'''
	f1 = open('san.log', 'r')
	print f1.read()
	f1.close()

def read_two():
	'''读取文件的第一行内容'''
	f1 = open('san.log', 'r')
	print f1.readline()
	f1.close()

def read_three():
	'''已行的方式读取文件的所有内容'''
	f1 = open('san.log', 'r')
	many=f1.readlines()
	for item in many:
		print item
	f1.close()

def fielWith():
	with open('san.log','r') as f:
		print f.read()

fielWith()


