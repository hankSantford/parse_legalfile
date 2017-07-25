#encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")#
import jieba
jieba.load_userdict("E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/userdict/userdict.txt")
import re#正则表达式

#分词匹配字段
accuser_dict = """ 原告 上诉人  申请再审人  再审申请人  原审上诉人  原审原告  申请人 检察院"""
defendant_dict = """被告 被上诉人 被申请人 再审被申请人 原审被上诉人 原审被告人 利害关系人"""
third_dict = """第三人 移送执行机关"""

#对待测试文本截取开始到第一个逗号，句号或换行符号的文本
def sign_spile():
	#测试文本
	test1 = "上诉人（原审被告人）毛程（绰号“阿天”），男，汉族，1987年1月2日出生，初中文化，户籍地湖南省衡阳市衡东县。因本案于2014年11月3日被羁押并被刑事拘留，同年12月4日被逮捕。"
	test2 = "中国人，中国字，"
	the1 = re.search(".*\uFF0C|.*\u3002|.*\n",test2)
	#print("value",the1.group(0))
	trule = re.compile(".*\uFF0C")
	t1 = re.match(".*\uFF0C", test2)
	#print("the test2", t1)
	te1 = re.split("\uFF0C|\u3002|\n", test1)
	#print("value", te1[0])
	




	# if the1 is None:
	# 	print("没有匹配到")
	# else:
	# 	s = the1.group(0)
	# 	print("thevalue",s)
	# 	#mark_a = re.compile(".*")

	# 	ii_a = mark_a.search(test1)
	# 	print(ii_a.group(0))

#sign_spile()

################
###
################
def  re_string_parse():

	testre1 = "（原一审被告、申诉人）成都泰来装饰工程有限公司"
	testre2 = "（原审原告）船舶信息研究中心（中国船舶重工集团公司第七一四研究所）"
	testre3 = "：济宁某航运（上海）有限公司"
	testre4 = "（原审被告）：李民"
	testre5 = "：关安钢"
	testre6 = " （一审原告）：舟山富生船舶修造有限公司。"

	testlist = [testre1,testre2,testre3,testre4,testre5,testre6]
	for item_stringlist in testlist:
		#如果以“（”或“：”开头，则将“（”至“）”之间忽略，提取“）”或“：”之后的字段
		#否则直接输出 
		a_test = re.search("^\uFF08|^\uFF1A|^\u0020",item_stringlist)
		if a_test is None:
			print("the value : ",item_stringlist)
		else:
			#print("the wit ca : ",a_test.group(0))
			#此时取“：”或“）”之后的.*值
			m = re.search("\uFF09", item_stringlist)
			if m is None:
				print("the value of m : ", item_stringlist)
				aim_string1 = re.search("[^\uFF1A].*|[^\u0020\uFF1A].*", item_stringlist)
				print("value a oa 1 : ", aim_string1.group(0))
			else:
				a_string = re.search("\uFF09.*", item_stringlist)
				aim_string = re.search("(?<=\uFF09).*", a_string.group(0))
				aim_string1 = re.search("[^\u0020\uFF1A].*|[^\uFF1A].*",aim_string.group(0))
				print("value b ob 1 : ",aim_string1.group(0))
		#print("the value of a_test : ",a_test)

#测试
re_string_parse()

#
accuser_list = ['a','b','c']
defendant_list = ['d','e','f']
third_list = []
A_value = [accuser_list,defendant_list,third_list]
B_key = ['原告','被告','第三方']
LAST = dict(zip(B_key,A_value))
print("the value of last : ", LAST)
