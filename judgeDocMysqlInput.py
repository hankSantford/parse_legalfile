#encoding=utf-8
import _mysql as mysql 
import re
import string

filePath = []

def DataInput(inde):
	#文件类型判别后导入可识别格式 ; 循环；列表；
	Path1 = "E:/PythonWorkSpace/legalInsParse/legalInsParseDemo/DataDemo/testDemo"
	Path2 = ".txt"	
	for i in range(inde):
		detpath = (Path1+str(i)+Path2) 
		filePath.append(detpath)
	return filePath

DataInput(80)

#链接到mysql数据库             连接方式     用户名      密码     数据库名
connect_mysql = mysql.connect("localhost","judgetest","123456","judgedoctest")
#cur = connect_mysql.query()
#本地文本存入数据库
def data_from_mysql(itempath):
	#获取连接的cursor
	try:
	#链接到mysql数据库             连接方式     用户名      密码     数据库名
		connect_mysql = mysql.connect("localhost","judgetest","123456","judgedoctest")
		with connect_mysql:
			cur = connect_mysql.cursor()
			
			for item in filePath:
				readfile = open(item).read()
				#print(readfile)
				iditem = 

	except mysql.Error,e:
		print("mysql Error ")
		connect_mysql.close()


data_from_mysql(filePath)
