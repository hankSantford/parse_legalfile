#encoding=utf-8
#将文本中的原告，被告，第三方，审批类型，受理法院，案件类别（事由）作为标签等，并返回为csv格式；
import re
import string
#caseCons = (casePaperName,judgeName,caseType,caseNumber,,caseDate)
#打开文件
testFile = []
filePath = []
parseFist = []#初步解析
parseTwice = []#二级解析
#解析文本信息列表字典存储[{key1:value1,key2:value2,...},{},...]
reTFJ = re.compile("\u4E00\u5BA1")#匹配“一审”字段
reTTJ = re.compile("\u4E8C\u5BA1")#匹配“二审”字段
reSup = re.compile("\u5BA1\u5224\u76D1\u7763")#匹配“审判监督”程序字段
reEF0 = re.compile("\u7279\u522B\u7A0B\u5E8F")#匹配“特别程序”
reEF1 = re.compile("\u7763\u4FC3\u7A0B\u5E8F")#“督促程序”字段
reEQ = re.compile("\u9009\u6C11\u8D44\u683C")#匹配"选民资格"字段
reEF = re.compile("\u516C\u793A\u50AC\u544A")#匹配"公示催告"程序必要字段
reER = re.compile("\u6267\u884C")#匹配“执行程序”字段
reZFL = re.compile("\u652F\u4ED8\u4EE4")#匹配“支付令”字段
reArbitration = re.compile("\u4EF2\u88C1")#匹配仲裁裁判书"仲裁"字段
#构造列表字典[{:},{},{},{},{},{},{}]
[{reTFJ:parseTFJ},{reTTJ:parseTTJ},{reSup:parseSup},{reEF0:parseEF},{reEQ:parseEQ},
{:parsePub},{:parseER},{rdefault:}]

#解析一审裁判文书以及审判监督程序中适用于一审程序的文件解析
def parseTFJ():
	print("适用于解析一审裁判文书")
#解析二审裁判文书以及审判监督程序中适用于二审程序的文件解析
def parseTTJ():
	print("适用于解析二审裁判文书")
#解析审判监督程序，判断其适用的具体程序类型为一审or二审
def parseSup():
	print("判断审判监督程序适用的解析裁判文书")
#解析特别程序和督促程序的裁判文书
def parseEF():
	print("适用于解析特别程序和督促程序的裁判文书")
#解析选民资格的裁判文书
def parseEQ():
	print("适用于解析选民资格裁判文书")
#解析公示催告程序裁判文书：Exigi Facias
def parseEF():
	print("适用于解析公示催告裁判文书")
#解析执行程序裁判文书
def parseER():
	print("适用于解析执行程序裁判文书")

#数据导入，
def DataInput(inde):
	#文件类型判别后导入可识别格式 ; 循环；列表；
	Path1 = "E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/DataDemo/testDemo"
	Path2 = ".txt"	
	for i in range(inde):
		detpath = (Path1+str(i)+Path2) 
		filePath.append(detpath)
	return filePath

DataInput(61)
#def judgeMark():

#文本解析:判决书，
def documentParse(doucList):
	#将文本列表开始按照\n\n分段并存入初步解析列表（parseFist）
	#解析字段：案件名称（xxx和xxx案由+审判状态xxx书），将确实抬头的文件路径进入二次解析列表存入
	for itempath in doucList:
		parsetItem = open(itempath,'r').read()
		spilefile = re.split("\n\n", parsetItem)
		#parseFist.append(spilefile)
		theFirstLine = spilefile[0]
		rec = re.compile("\u4E66")
		#print(rec.search(theFirstLine))
		if rec.search(theFirstLine) is None:
			print("121")
			parseTwice.append(itempath) 
			print(itempath)
			judgeName = spilefile[1]
			caseType = spilefile[2]
			caseNumber = spilefile[3]
			#caseDate0 = spilefile[len(spilefile)-2]
			print(judgeName,caseType,caseNumber)
		else:
			#print(itempath)
			caseName = spilefile[0]
			judgeName = spilefile[1]
			caseType = spilefile[2]
			caseNumber = spilefile[3]
			#caseDate0 = spilefile[len(spilefile)-2]
			print(caseName,judgeName,caseNumber,caseType)

		#缩小诉讼人和被诉讼人的解析范围	
		testdict = dict(zip(range(len(spilefile)),spilefile))
		Lo = []
		for key,value in testdict.items():	
			#88C1 5B9A
			stopMark = re.search("\u5BA1\u7406", value)
			if stopMark is None:
				continue
			else:#返回该段落的序号
				s = stopMark.group(0)
				mark1 = re.compile("\n.*"+s+".*\n")
				mark1.search(value)
				Lo.append(key)
				#print(key,value)
			stopflag = Lo[0]
		print(stopflag)
		#文件解析时候直接提取stopflag，如果为空则全文解析查找需要的字段，
		#构造匹配字典{key:value}
		
		
	return parseTwice

	#从初步解析文本中取出有关于起诉方，应诉方，相关第三方的文本信息
documentParse(filePath)




