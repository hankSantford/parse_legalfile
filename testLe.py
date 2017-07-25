# -*- coding: utf-8 -*-
import re
import string

testD = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo18.txt').read()
testK = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo60.txt').read()
test1 = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo1.txt').read()
test2 = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo4.txt').read()
test3 = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo52.txt').read()
test4 = open(r'E:\PythonWorkSpace\legalInsParse\legalInsParseDemo\DataDemo\testDemo9.txt').read()
test = [testD,testK,test1,test2,test3,test4]


for item in test:
	#trt = re.search("\u539F\u544A\uFF09", item[:1000])
	itsp = []
	itsp = re.split(r'\n', item)
	#案件号解析
	caseNumer = itsp[6]
	print("caseNumer:"+caseNumer)
	print(itsp[8])
	for itemm in itsp[8:]:
		if isinstance(item,list):
			print("oop")	
		else:
			parseTest = []
			parseTest1 = []
			parseTest = re.findall("\u539F\u544A.*?\。",itemm)
			lei = len(parseTest[0])
			for i in parseTest:
				if isinstance(i,list):
					print()
				else:
					if (len(i) > lei) or (len(i) == 0):
						parseTest.remove(i)
						print(i)

			parseTest1 = re.findall("\u88AB\u544A.*?\。", itemm)
#匹配到第一个被告时候就采取如下，反之就继续循环匹配
			print(len(parseTest1))
			leii = len(parseTest1[0])
			for ii in parseTest1:
				if isinstance(ii, list) | len(set(parseTest1)) == 0:
					print()
				else:
					if len(ii) > leii:
						parseTest1.remove(ii)
			print(parseTest1)

			#if len(set(parseTest)) == 0:
			#	print("")
			#else:
			#	print(set(parseTest))
			#if len(set(parseTest1)) == 0:
			#	print("")
			#else:
			#	print(set(parseTest1))

	