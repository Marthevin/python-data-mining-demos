# -*- coding:utf-8 -*-

fp = open("file1.txt")

for line in fp:
	f = line.rstrip("\r\n").split("\t")
	print f[0] + "###" + f[1]
	