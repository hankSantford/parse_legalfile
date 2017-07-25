#encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")#
import jieba
jieba.load_userdict("E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/userdict/userdict.txt")
import re
import json #输出为json格式

#mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo", "acata"]
#testlist = [["this sis a amazing day!"],
#			["we have a good time!"],
#			["this sis a great trivel sin summer!"],
#			["Did you have a never forgive thing sin this year?"],
#			["every wonderful day!"],
#			["this stype can snot be accepted!"],
#			["The Great Wall has been a sign sfor sall over the world"],
#			["Django ssis a very prefect construction around the python web!"],
#			["You always early to go school!"]]
#r = re.compile(r".*ca")
#newlist = list(filter(r.match, mylist))
#print(newlist)
#for new in newlist:
#	print(mylist.index(new))
# enumerate()
#s = [index for index, item in enumerate(mylist) if re.search(r".*cat", item)]
#print([index for index, item in enumerate(mylist) if re.search(r".*cat", item)])
#
#rm = re.compile("ama.*\s")
#
#dictest = dict(zip(range(len(testlist)),testlist))
#print(dictest)
#for key in dictest:
#	print(key)
#for key,value in dictest.items():
#	print(key,type(value))
#按照值查询字典并返回
#for key,value in dictest.items():
#	if isinstance(value,list):
#		for item in value:
#			tut = re.search(".*ama.*", item)
#			if tut is None:
#				continue
#			else:
#				tut.group(0) == item 
#				print(key,value)
#	else:
#		print("...")
###############################################################################################
testFile = []
filePath = []
parseFist = []#初步解析
parseTwice = []#二级解析
#Lo = []#将每个分段后字典化的文本含有特别停止字段的key返回该列表
stopM = []#在每次循环中从Lo()中取第一个存入，
StartL = []#记录开始解析的位置，当被解析文档有题目时候记录从第四行开始反之从第三行开始
sl = {}
spilefile = []
inde = 135#测试数据的规模
#解析文本信息列表字典存储[{key1:value1,key2:value2,...},{},...]
# reTFJ = re.compile("\u4E00\u5BA1")#匹配“一审”字段
# reTTJ = re.compile("\u4E8C\u5BA1|\u518D\u5BA1")#匹配“二审”字段
# reSup = re.compile("\u5BA1\u5224\u76D1\u7763")#匹配“审判监督”程序字段
# reEF0 = re.compile("\u7279\u522B\u7A0B\u5E8F")#匹配“特别程序”
# reEF1 = re.compile("\u7763\u4FC3\u7A0B\u5E8F")#“督促程序”字段
# reEQ = re.compile("\u9009\u6C11\u8D44\u683C")#匹配"选民资格"字段
# rePub = re.compile("\u516C\u793A\u50AC\u544A")#匹配"公示催告"程序必要字段
# reER = re.compile("\u6267\u884C")#匹配“执行程序”字段
# reZFL = re.compile("\u652F\u4ED8\u4EE4")#匹配“支付令”字段
# reArbitration = re.compile("\u4EF2\u88C1")#匹配仲裁裁判书"仲裁"字段

# #!#解析一审裁判文书以及审判监督程序中适用于一审程序的文件解析
# def parseTFJ(thefile):
# 	print("适用于解析一审裁判文书")
# 	#print(thefile)
# 	#解析原告和被告,解析的数据存入集合
# 	defendantSet = []
# 	accuserSet = []
# 	ThirdParty = []
# 	for item in thefile[:Lo[0]]:
# 		#解析原告字段
# 		ait = re.findall("\u539F\u544A.*?\。", item)
# 		for i in ait:
# 			if i is None:
# 				continue
# 			else:
# 				accuserSet.append(i)
# 		#解析被告字段
# 		dit = re.findall("\u88AB\u544A.*\。", item)
# 		for i in dit:
# 			if i is None:
# 				continue
# 			else:
# 				defendantSet.append(i)
# 		#解析第三人字段
# 		tit = re.findall("\u7B2C\u4E09\u4EBA.*?\。", item)
# 		for i in tit:
# 			if i is None:
# 				continue 
# 			else:
# 				ThirdParty.append(i)
# 	#将存入集合的原被告集合做差集得到原告集合
# 	#accuserSet = accuserSet0 - defendantSet
# 	print(accuserSet)
# 	print(defendantSet)
# 	print(ThirdParty)
# 	return accuserSet,defendantSet,ThirdParty

# #!#解析二审裁判文书以及审判监督程序中适用于二审程序的文件解析
# def parseTTJ(thefile):#
# 	print("适用于解析二审裁判文书")
# 	#解析上诉人，和被上诉人，并存入集合
# 	accuserSet0 = []
# 	defendantSet = []
# 	accuserSet = []
# 	ThirdParty = []
	
# 	for item in thefile[:Lo[0]]:
# 		ait = re.findall("\u4E0A\u8BC9\u4EBA.*?\。", item)
# 		for i in ait:
# 			if i is None:
# 				continue
# 			else:
# 				#m =re.findall("(?<=\u4E0A\u8BC9\u4EBA).*(?=\。)", i)
# 				accuserSet0.append(i)
# 		dit = re.findall("\u88AB\u4E0A\u8BC9\u4EBA.*?\。", item)
# 		for i in dit:
# 			if i is None:
# 				continue
# 			else:
# 				defendantSet.append(i)
# 		tit = re.findall("\u7B2C\u4E09\u4EBA.*?\。", item)
# 		for i in tit:
# 			if i is None:
# 				continue
# 			else:
# 				ThirdParty.append(i)

# 	#accuser = set(accuserSet0) - set(defendantSet)
# 	print(accuserSet0)
# 	print(defendantSet)
# 	print(ThirdParty)
# #!#解析审判监督程序，判断其适用的具体程序类型为一审or二审
# def parseSup(thefile):
# 	print("判断审判监督程序适用的解析裁判文书")

# #!#解析特别程序和督促程序（支付令）的裁判文书
# def parseEF(thefile):
# 	print("适用于解析特别程序和督促程序（含支付令）的裁判文书")
# 	#解析申请人和被申请人
# 	defendantSet = []
# 	accuserSet = []
	
# 	for item in thefile[:Lo[0]]:
# 		#解析申请人
# 		ait = re.findall("\u7533\u8BF7\u4EBA.*?\。", item)
# 		for i in ait:
# 			if i is None:
# 				continue
# 			else:
# 				#m =re.findall("(?<=\u4E0A\u8BC9\u4EBA).*(?=\。)", i)
# 				accuserSet.append(i)
# 		#解析被申请人
# 		dit = re.findall("\u88AB\u7533\u8BF7\u4EBA.*?\。", item)
# 		for i in dit:
# 			if i is None:
# 				continue
# 			else:
# 				defendantSet.append(i)
# 	#做差集
# 	#accuserSet = accuserSet0 - defendantSet
# 	print(accuserSet)
# 	print(defendantSet)

# #!#解析选民资格的裁判文书
# def parseEQ(thefile):
# 	print("适用于解析选民资格裁判文书")
# 	#选民资格案件中需要解析的是起诉人（有时也做申请人），被起诉人，负责人（角色如第三方）
# 	accuserSet0 = []
# 	defendantSet = []
# 	accuserSet = []
# 	ThirdParty = []
	
# 	for item in thefile[:Lo[0]]:
# 		#解析申请人
# 		ait = re.findall("\u7533\u8BF7\u4EBA.*?\。", item)
# 		for i in ait:
# 			if i is None:
# 				continue
# 			else:
# 				#m =re.findall("(?<=\u4E0A\u8BC9\u4EBA).*(?=\。)", i)
# 				accuserSet0.append(i)
# 		#解析被起诉人字段
# 		dit = re.findall("\u88AB\u8D77\u8BC9\u4EBA.*?\。", item)
# 		for i in dit:
# 			if i is None:
# 				continue
# 			else:
# 				defendantSet.append(i)
# 		#解析负责人字段
# 		tit = re.findall("\u8D1F\u8D23\u4EBA.*?\。", item)
# 		for i in tit:
# 			if i is None:
# 				continue
# 			else:
# 				ThirdParty.append(i)
# 	#做差集
# 	#accuserSet = accuserSet0 - defendantSet
# 	print(accuserSet)
# 	print(defendantSet)
# 	print(ThirdParty)

# #!#解析公示催告程序裁判文书：Exigi Facias
# def parsePub(thefile):
# 	print("适用于解析公示催告裁判文书")
# 	#催告裁判文书中需要解析的字段是申请人，利害关系人
# 	defendantSet = []
# 	accuserSet = []
	
# 	for item in thefile[:Lo[0]]:
# 		#解析申请人
# 		ait = re.findall("\u7533\u8BF7\u4EBA.*?\。", item)
# 		for i in ait:
# 			if i is None:
# 				continue
# 			else:
# 				#m =re.findall("(?<=\u4E0A\u8BC9\u4EBA).*(?=\。)", i)
# 				accuserSet.append(i)
# 		#解析利害关系人
# 		dit = re.findall("\u5229\u5BB3\u5173\u7CFB\u4EBA.*?\。", item)
# 		for i in dit:
# 			if i is None:
# 				continue
# 			else:
# 				defendantSet.append(i)#有时利害关系人并没有在裁判文书中出现具体的对象
# 	#做差集
# 	#accuserSet = accuserSet0 - defendantSet
# 	print(accuserSet)
# 	print(defendantSet)
	
# #!#解析执行程序裁判文书
# def parseER(thefile):
# 	print("适用于解析执行程序裁判文书")
# 	#解析申请执行人（有时写作：移送执行机关），被执行人字段
# 	defendantSet = []
# 	accuserSet = []
	
# 	for item in thefile[:Lo[0]]:
# 		#解析申请人
# 		ait = re.findall("\u7533\u8BF7\u6267\u884C\u4EBA.*?\。", item)
# 		for i in ait:
# 			if i is None:
# 				continue
# 			else:
# 				#m =re.findall("(?<=\u4E0A\u8BC9\u4EBA).*(?=\。)", i)
# 				accuserSet.append(i)
# 		#解析被申请人
# 		dit = re.findall("\u88AB\u7533\u8BF7\u6267\u884C\u4EBA.*?\。", item)
# 		for i in dit:
# 			if i is None:
# 				continue
# 			else:
# 				defendantSet.append(i)
# 	#做差集
# 	#accuserSet = accuserSet0 - defendantSet
# 	print(accuserSet)
# 	print(defendantSet)
# #!#解析仲裁裁判文书
# def parseArbitration(thefile):
# 	print("适用于解析仲裁裁判文书")
# 	accuserSet = []
# 	defendantSet = []
# 	ThirdParty = []
# 	#解析申请人，被申请人，第三方
# 	for item in thefile[:Lo[0]]:
# 		#解析申请人
# 		ait = re.findall("\u7533\u8BF7\u4EBA.*?\。", item)
# 		for i in ait:
# 			if i is None:
# 				continue
# 			else:
# 				#m =re.findall("(?<=\u4E0A\u8BC9\u4EBA).*(?=\。)", i)
# 				accuserSet.append(i)
# 		#解析被申请人
# 		dit = re.findall("\u88AB\u7533\u8BF7\u4EBA.*?\。", item)
# 		for i in dit:
# 			if i is None:
# 				continue
# 			else:
# 				defendantSet.append(i)
# 		#解析第三方
# 		tit = re.findall("\u7B2C\u4E09\u4EBA.*?\。", item)
# 		for i in tit:
# 			if i is None:
# 				continue
# 			else:
# 				ThirdParty.append(i)
# 	#做差集
# 	accuserSet = accuserSet0 - defendantSet
# 	print(accuserSet)
# 	print(defendantSet)
# 	print(ThirdParty)

# #!#解析无标题的裁判文书？？？？？？？？？？？？？？？？？
# def parseRdefault(thefile):
# 	print("由于裁判文书标题缺失，需要使用默认程序解析")

#构造字典{:,:,:,:,:,:,:}用于字段匹配键，返回值函数进行解析
#seldict = {reTFJ:parseTFJ,reTTJ:parseTTJ,reSup:parseSup,reEF0:parseEF,reEF1:parseEF,
#reEQ:parseEQ,rePub:parsePub,reER:parseER,reZFL:parseEF,reArbitration:parseArbitration}

#数据导入
def DataInput(inde):
	#文件类型判别后导入可识别格式 ; 循环；列表；
	Path1 = "E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/DataDemo/testDemo"
	Path2 = ".txt"	
	for i in range(inde):
		detpath = (Path1+str(i)+Path2) 
		filePath.append(detpath)
	return filePath

DataInput(inde)
#文本解析:判决书，
def documentParse(doucList,inde):
	Lo=[]#将每个分段后字典化的文本含有特别停止字段的key返回该列表
	#将文本列表开始按照\n\n分段并存入初步解析列表（parseFist）
	#解析字段：案件名称（xxx和xxx案由+审判状态xxx书），将确实抬头的文件路径进入二次解析列表存入
	for itempath in doucList:
		parsetItem = open(itempath,'r').read()
		spilefile = re.split("\n\n", parsetItem)
		parseTwice.append(spilefile)
		theFirstLine = spilefile[0]
		#匹配“书”\u4E66或者“案”\u6848
		rec = re.compile("\u4E66|\u6848")
		if rec.search(theFirstLine) is None:
			#print("121")
			#parseTwice.append(itempath) 
			#print(itempath)
			judgeName = spilefile[0]
			caseType = spilefile[1]
			caseNumber = spilefile[2]
			StartL.append(3)
			
		else:
			#print(itempath)
			caseName = spilefile[0]
			judgeName = spilefile[1]
			caseType = spilefile[2]
			caseNumber = spilefile[3]
			StartL.append(4)
		#print(StartL)
		#print(len(StartL))
		#缩小诉讼人和被诉讼人的解析范围	
		testdict = dict(zip(range(len(spilefile)),spilefile))
		#print(testdict)
		#返回诉讼参与人解析的截止点
		for key,value in testdict.items():	
			#88C1 5B9A
			li = len(Lo)
			print(li)
			#print("11111")
			#匹配审理
			stopMark = re.search("\u5BA1\u7406|\u5BA1\u67E5", value)
			if stopMark is None:
				#continue
				#匹配裁定字段
				stopMark2 = re.search("\u88C1\u5B9A\u5982\u4E0B", value)
				if stopMark2 is None:
					continue
				else:
					s = stopMark2.group(0)
					mark2 = re.compile(".*"+s+".*")

					mark2.search(value)
					#print("mark2",value)
					Lo.append(key)
			di = len(Lo) - li
			if di == 1:
				break

			else:#返回该段落的序号
				s = stopMark.group(0)
				mark1 = re.compile(".*"+s+".*")
				mark1.search(value)
				Lo.append(key)

				#print(itempath)
			print(", ...",value)
			print(len(Lo))
			dl = len(Lo) - li
			if dl == 1:
				break
	#print("ppppp",Lo)
	#print(len(Lo))

		#将字段起止位置构造成字典key是文件号，value是一个二元元组第一个是起点，第二个是截止点

		#print(stopM[8][0])
		#for item in spilefile[4:Lo[0]]:
			#parseFist.append(item)
#??????????????????????????????????????????????????????????
	#for key,value in seldict.items():
	#	mk = key.search(theFirstLine) 
	#	if mk is None:
	#		#print(key,theFirstLine,"can not parse this file ")
	#		continue
	#	else:
			#print(value(spilefile))
	#		value(parseFist)
			#print(key,theFirstLine)

	#从初步解析文本中取出有关于起诉方，应诉方，相关第三方的文本信息
		#for itemline in spilefile[:stopflag]:
	a = []
	for i in range(inde):
		a.append(i)
	#生成开始位置字典
	#解析起始位置字典
	sl = dict(zip(a,StartL))
	si = dict(zip(a,Lo))
	#print("the start ",sl)
	#print("the stop flag", si)
	#
	stuts = []
	for key,value in sl.items():
		slkey = key
		slvalue = value
		for key,value in si.items():
			if key == slkey:
				tut = (slvalue,value)
				stuts.append(tut) 
				#print("sivalue:", value)
				#print("slvalue:", slvalue)

	#print(stuts)
	theflag = dict(zip(a,stuts))
	#print("aaaaaaaaa",dict(zip(a,stuts)))

	return theflag #parseTwice,parseFist

theflag_ss = documentParse(filePath,inde)#获得起始和结束位置节点

##############################################################################

########################################################################
for item in parseTwice:
	print(len(item))
	for ite in item[3:10]:
		print("the value of ite",ite)
#列表推导式
print("列表推到狮子",[len(item) for item in parseTwice])

#匹配有冒号的行，进行解析
def colonparse(thelined):
	pass
#匹配有右括号的行，进行解析
def bracketparse(thelined):
	pass
#匹配无冒号，右括号的行，有人和告字样的，进行解析
def specharparse(thelined):
	pass
#匹配冒号到逗号或者句号
colon = re.compile("\uFF1A")
#匹配右括号
rightbracket = re.compile("\uFF09")
#匹配人或着告
spechar = re.compile("\u4EBA|\u544A")
#构造匹配字符调用函数的字典
chpardic = {colon:colonparse,rightbracket:bracketparse,spechar:specharparse}
# for key,value in theflag_ss.items():
# 	print("the value of the start : ", value[0])
###############################################################################
###将获取的起始和截止位置theflage_ss传入解析函数：def DefaultParse
###############################################################################
#定义适用于所有类型的裁判文书的解析函数
#参数：文件，文件解析的起止位置字典
def DefaultParse(theParseTwice,theflag):
	#按照文本的序号查找对应值开启解析
	#print("value", len(theParseTwice))
	# for itme in theParseTwice:
	# 	print("aoopp:", itme[0],len(itme))
	accuser_dict = """ 原告 上诉人  债权人  申请再审人  再审申请人  申请执行人  原审上诉人  原审原告  申请人  检察院  公诉机关"""
	defendant_dict = """被告 被上诉人 债务人  被申请人 再审被申请人 被申请执行人  原审被上诉人 原审被告人  原公诉机关  利害关系人"""
	third_dict = """第三人  第三方  移送执行机关"""
	tpt = []
	for i in range(inde):
		tpt.append(i)
	tptdict = dict(zip(tpt,theParseTwice))
	thelastlist = []#save the dict by parsed
	#验证程序
	# for key,value in tptdict.items():
	# 	print("the value of tptdict", key ,value[0])
	#采用生成器读取文本item——file

	for key,value in theflag_ss.items():
		file_id = key
		start_flag = value[0]
		end_flag = value[1]
		#################################################################################
		accuser_list = []
		defendant_list = []
		third_list = []
		A_value = [accuser_list,defendant_list,third_list]
		B_key = ['原告','被告','第三方']
		#################################################################################
		for key ,value in tptdict.items():
			if file_id == key:
				print("the id file : ", key )
				a = value[start_flag:end_flag]
				print("the value of a :", len(a),a)
				#将第一个匹配到换行符，句号，逗号的句子提取出来并转为字符
				###################################################################
				sub_a = []
				for i_a in a:
					#print("the value of i_a : ", i_a)
					sub_ia = re.split("\uFF0C|\u3002|\n", i_a)
					#print("the value of sub_ia : ", sub_ia)
					cw = jieba.cut(sub_ia[0],cut_all=False)
					#print("the value of cw ； ","/".join(cw))\
					#cs = "".join(cw)
					for sub_cw in cw:
						if sub_cw in accuser_dict:
							#print("the 分词后的词","".join(sub_cw))
							if sub_cw == "人" or sub_cw == "原审":
								continue
							#将诉讼提起方的字段提取出来
							#匹配格式：
							# 1. 冒号或人或告或右括号为开头，以逗号，句号或者换行符为截止的
							# 2. 
							
							# 	accuser_string = re.search("","".join(cw))
							else:
								cws = "".join(cw)
								a_test = re.search("^\uFF08|^\uFF1A",cws)
								if a_test is None:
									accuser_list.append(cws)
									#print("诉讼提起方: ",cws)

								else:
									#print("the wit ca : ",a_test.group(0))
									#此时取“：”或“）”之后的.*值
									m = re.search("\uFF09", cws)
									if m is None:
										#print("the value of m : ", cws)
										aim_string1 = re.search("[^\uFF1A].*|[^\u0020\uFF1A].*|[^\u0020\uFF1A\u0020].*", cws)
										accuser_list.append(aim_string1.group(0))
										#print("诉讼提起方：", aim_string1.group(0))
									else:
										a_string = re.search("\uFF09.*", cws)
										aim_string = re.search("(?<=\uFF09).*", a_string.group(0))
										aim_string1 = re.search("[^\u0020\uFF1A].*|[^\uFF1A].*",aim_string.group(0))
										accuser_list.append(aim_string1.group(0))
										#print("诉讼提起方：",aim_string1.group(0))
								#A_value.append(accuser_list)
								print("原告", accuser_list)
						else:
							if sub_cw in defendant_dict:
								#将诉讼提起方的字段提取出来
								#匹配格式：
								# 1. 冒号或人或右括号为开头，以逗号，句号或者换行符为截止的
								# 2. 
								#defendant_string = re.search("pattern","".join(cw))
								cws = "".join(cw)
								a_test = re.search("^\uFF08|^\uFF1A",cws)
								if a_test is None:
									defendant_list.append(cws)
									#print("被诉讼方: ",cws)
								else:
									#print("the wit ca : ",a_test.group(0))
									#此时取“：”或“）”之后的.*值
									m = re.search("\uFF09", cws)
									if m is None:
										#print("the value of m : ", cws)
										aim_string1 = re.search("[^\uFF1A].*|[^\u0020\uFF1A].*|[^\u0020\uFF1A\u0020].*", cws)
										defendant_list.append(aim_string1.group(0))
										#print("被诉讼方：", aim_string1.group(0))
										#print("诉讼提起方 ： ",aim_string1.group(0))
									else:
										a_string = re.search("\uFF09.*", cws)
										aim_string = re.search("(?<=\uFF09).*", a_string.group(0))
										aim_string1 = re.search("[^\u0020\uFF1A].*|[^\uFF1A].*",aim_string.group(0))
										defendant_list.append(aim_string1.group(0))
										#print("被诉讼方：",aim_string1.group(0))
								print("被告：", defendant_list)
							else:
								if sub_cw in third_dict:
									#将诉讼提起方的字段提取出来
									#匹配格式：
									# 1. 冒号或人或右括号为开头，以逗号，句号或者换行符为截止的
									# 2. 
									#third_string = re.search("pattern","".join(cw))
									cws = "".join(cw)
									a_test = re.search("^\uFF08|^\uFF1A",cws)
									if a_test is None:
										third_list.append(cws)
										#print("the value cws : ",cws)
									else:
										#print("the wit ca : ",a_test.group(0))
										#此时取“：”或“）”之后的.*值
										m = re.search("\uFF09", cws)
									
										if m is None:
											#print("the value of m : ", cws)
											aim_string1 = re.search("[^\uFF1A].*|[^\u0020\uFF1A].*|[^\u0020\uFF1A\u0020].*", cws)
											third_list.append(aim_string1.group(0))
											#print("第三方：", aim_string1.group(0))
											#print("诉讼提起方 ： ",aim_string1.group(0))
										else:
											a_string = re.search("\uFF09.*", cws)
											aim_string = re.search("(?<=\uFF09).*", a_string.group(0))
											aim_string1 = re.search("[^\u0020\uFF1A].*|[^\uFF1A].*",aim_string.group(0))
											third_list.append(aim_string1.group(0))
											#print("第三方：",aim_string1.group(0))
									print("第三方 ：",third_list)
		#print("value", A_value)
		the_last = dict(zip(B_key,A_value))
		thelastlist.append(the_last)
		#ajson = json.dumps(thelastlist,sort_keys = True,indent = 2,ensure_ascii=False)
		turn_json = json.dumps(thelastlist,ensure_ascii=False)
		#print("the value of the last dict",the_last)
	#print("the last list : ",ajson)
	return turn_json
#############################################################################################################
		#先匹配每行中含有原告，上诉人，原审原告，申请人，申请再审人，再审申请人，原审上诉人，申请执行人，
		#accuserSide = re.compile("pattern")
		#匹配每行中含有被告，被上诉人，原审被告，被申请人，再审被申请人，原审被上诉人，被执行人，
		#defendantSide = re.compile("pattern")
		#冒号或人或右括号为开头，以逗号，句号或者换行符为截止的
		#lead_trail = re.compile("pattern")
		#返回这些字段所在的行号并在这些行号的基础上

		##进行第二次解析，匹配是否有冒号有则从冒号到逗号或句号
		##如果没有冒号先匹配有否右括号，如果有则从此开始解析到逗号或句号结束

		#没有冒号和由括号的，如果有从人或告字开始，逗号，句号结束，
		#通过建立解析字典函数完成二次解析

#利用theflag作为一个输入的参数进入第二次解析
thelastlist = DefaultParse(parseTwice, theflag_ss)

##############################################################################################################
##############################################################################################################
######将解析的结果输出成为txt文本######
######实现功能：                 ######
###### 1. 将解析出的字段输出为txt文本格式的文件中保存；######
###### 2. 将已经解析的文本和未能解析的文本占总解析量的比例计算并输出；######
##############################################################################################################
# def txt_json_output(thelastlist):
# 	print("value", thelastlist)
	
# txt_json_output(thelastlist)