#!/usr/bin/env python 
#-*-coding:utf-8-*-


def div(a,b):
	try:
		print  a/b
	except BaseException as e:
		print e.args
	except Exception as e:
		print e.args
	except TypeError as e:
		print e.args
	except ValueError as e:
		print e.args
	except ReferenceError as e:
		print e.args
	except ZeroDivisionError as e:
		print u'代码执行异常'
		print e.args
	else:
		print u'我是else，我骄傲'
	finally:
		print u'不管成功与失败，我都执行'

div(2,1)
