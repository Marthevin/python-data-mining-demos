# -*- coding:utf-8 -*-

import map_reduce

def reduce_function(data):
	V1 = {}
	for d in data:
		i = d[0]
		if i not in V1:
			V1[i] = 0
		V1[i] = V1[i] + d[1]
		
	for i in V1:
		map_reduce.reduce_output(i, V1[i])