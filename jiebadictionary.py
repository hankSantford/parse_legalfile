#encoding=utf-8
from __future__ import print_function, unicode_literals
import re
import sys
sys.path.append("E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/DataDemo")#可以自定义之
import jieba
jieba.load_userdict("E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/DataDemo/testjudge.txt")
import jieba.posseg as pseg #添加词典

#动态添加词典

testfile = []
testline = []
#数据导入
datafile = open("E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/DataDemo/testDemo1.txt").read()
testfile = re.split("\n\n", datafile)
#自定义分词次词典，
print(jieba.suggest_freq('上诉人', True))
for itemline in testfile[3:12]:
	#对文本分析时应该采用的是精确分词即：精确分词
	theline = jieba.cut(itemline,cut_all=False)#切词生成的对象是生成器对象
	print("De Mode::"+" ".join(theline))
	#print(type(jieba.cut(itemline,cut_all=False)))
	#testline.append(theline)

#然后模式识别诉讼提请方和诉讼接受方
