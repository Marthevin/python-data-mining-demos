# -*- coding:utf-8 -*-

import map_reduce

def map_function(data):
	fp = open("V0")
	V0 = []
	for line in fp:
		V0.append(float(line.rstrip("\r\n")))
		
	j = 0
	for d in data:
		f = d.rstrip("\r\n").split("\t")
		for i in range(0, len(f)):
			mij = float(f[i])
			map_reduce.map_output(i, mij * V0[j])