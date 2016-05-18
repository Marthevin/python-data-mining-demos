# -*- coding:utf-8 -*-

fp = open("file1.txt")

for line in fp:
	print line.rstrip("\r\n")