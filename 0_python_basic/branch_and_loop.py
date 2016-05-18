# -*- coding:utf-8 -*-

#分支
a = 0
b = 1
if a == 0 and b == 1:
	print "Branch1"
elif a == 2 or b == 2:
	print "Branch2"
elif not (a == 1):
	print "Branch3"
	
b = {}
b["china"] = "beijing"
b["france"] = "paris"
if "china" in b:
	print "china"
if "japan" not in b:
	print "not japan"
	
#对数组循环
a = [0, 1, 1, 2, 3, 5, 8]
for i in range(0, len(a)):
	print a[i]
	
for v in a:
	print v
	
#对查找表循环
b = {}
b["china"] = "beijing"
b["france"] = "paris"
for key in b:
	print key, b[key]
	
#无限循环与跳出
i = 0
while True:
	print i
	i = i + 1
	if i == 5:
		break