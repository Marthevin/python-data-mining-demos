# -*- coding:utf-8 -*-

import map_reduce

def reduce_function(data):
	for d in data:
		map_reduce.reduce_output(d[0], d[1][0] + "\t" + d[1][1])