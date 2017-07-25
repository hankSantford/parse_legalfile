#encoding=utf-8
from __future__ import print_function , unicode_literals
import re
import string
import numpy as np
from mvpa2.tutorial_suite import *

import sys
sys.path.append("E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/DataDemo")#可以自定义之
import jieba
jieba.load_userdict("E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/DataDemo/testjudge.txt")
import jieba.posseg as pseg #词性标记

jieba.add_word('word')
jieba.add_word('word')
jieba.add_word('word')
#testQ = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo0.txt').read()
#testP = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo34.txt').read()
#testO = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo52.txt').read()
testA = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo1.txt').read()
testB = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo3.txt').read()
testC = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo15.txt').read()
#testD = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo18.txt').read()
#testE = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo24.txt').read()
#testF = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo27.txt').read()
#testG = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo39.txt').read()
#testH = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo42.txt').read()
#testI = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo46.txt').read()
#testJ = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo57.txt').read()
#testK = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo60.txt').read()
#test = [testQ,testP,testO,testA,testB,testC,testD,testE,testF,testG,testH,testI,testJ,testK]
test = [testA,testB,testC]
#for item in test:
	#isinstance(type(re.search("\u7533\u8BF7\u4EBA", item)),NoneType)
#	trt = re.search("\u539F\u544A\uFF09", item[:500])
	#print(str(trt))
#	if trt is None:
#		parseFirstf = re.findall("", item)
#		parseTest = re.findall("(?<=\u539F\u544A).*?(?=\。)",item)
#		parseTest1 = re.findall("(?<=\u88AB\u544A).*?(?=\，)", item)
#		print("此案为一审案件")
#		print(set(parseTest))
#		print(set(parseTest1))
#		#print(item[:100])
#		trt1 = re.search("\u7533\u8BF7\u4EBA", item[:500])
#		if trt1 is None:
#			print("OVER!!!")
#		else:
#			parseTest = re.findall("(?<=\u7533\u8BF7\u4EBA).*?(?=\。)",item)
#			parseTest1 = re.findall("(?<=\u88AB\u7533\u8BF7\u4EBA).*?(?=\，)", item)
#			print("此案为民事仲裁类案件")
#			print(set(parseTest)) 
#			print(set(parseTest1))
#			#print(item[:100])
#
#	else:
#		parseTest = re.findall("\u4E0A\u8BC9\u4EBA.*?\。", item[:500])
#		parseTest1 = re.findall("\u88AB\u4E0A\u8BC9\u4EBA.*?\。", item[:500])
#		print("此案为二审案件")
#		print(set(parseTest))
#		print(len(set(parseTest)))
#		print(set(parseTest1))
#		print(len(set(parseTest1)))
#		#print(item[:100])
#构造字典列表完成switch case 功能
#fieldoc = ["中国中信集团有限公司与江苏中信建设集团有限公司、江苏中信建设集团有限公司南京分公司侵害商标权纠纷二审民事判决书",
#			"浙江阿里巴巴电子商务有限公司与周容、周建等网络服务合同纠纷一审民事判决书",
#			"广东中海航建设集团有限公司与刘静，李峰建设合同纠纷一案二审民事判决书"]
#reTFJ = re.compile("\u4E00\u5BA1")#匹配“一审”字段
#reTTJ = re.compile("\u4E8C\u5BA1")#匹配“二审”字段
#reSup = re.compile("\u5BA1\u5224\u76D1\u7763")#匹配“审判监督”程序字段
#reEF0 = re.compile("\u7279\u522B\u7A0B\u5E8F")#匹配“特别程序”
#reEF1 = re.compile("\u7763\u4FC3\u7A0B\u5E8F")#“督促程序”字段
#reEQ = re.compile("\u9009\u6C11\u8D44\u683C")#匹配"选民资格"字段
#rePub = re.compile("\u516C\u793A\u50AC\u544A")#匹配"公示催告"程序必要字段
#reER = re.compile("\u6267\u884C")#匹配“执行程序”字段
#reZFL = re.compile("\u652F\u4ED8\u4EE4")#匹配“支付令”字段
#reArbitration = re.compile("\u4EF2\u88C1")#匹配仲裁裁判书"仲裁"字段
#def parseTFJ(thefile):
#	print("适用于解析一审裁判文书")
	#print(thefile)
	#解析原告和被告,解析的数据存入集合

#!#解析二审裁判文书以及审判监督程序中适用于二审程序的文件解析
#def parseTTJ(thefile):
	#解析上诉人，和被上诉人，并存入集合
#	print("适用于解析二审裁判文书")

#m = {reTFJ:parseTFJ,reTTJ:parseTTJ}
	
#for item in fieldoc:
#	for key ,value in m.items():
#		iu = key.search(item)
#		if iu is None:
#			print(key,"can not match value function")
#			continue 
#		else:
#			print(key,"here is starting parse")
#			value(item)
#			print(value)
#生成器使用 
def countdown(n):
	#print("counting down")
	while n >0:
		yield n
		n -=1
	
m = countdown(10)
m.__next__()
m.__next__()
#print(type(m))
#
 
#print(ad[4])
for ifile in test:
	afile = re.split("\n\n", ifile)
	for item in afile[4:11]:
		#itemp0 = jieba.cut(item,cut_all=True)#全模式
		itemp1 = jieba.cut(item,cut_all=False)#
		#itemp2 = jieba.cut_for_search(item)#搜索引擎模式
		
		print(item)
		print("Full Mode:"+"/".join(itemp1))
			
		#print("Default Mode:"+"/".join(itemp1))
		#print(","+"/".join(itemp2))

