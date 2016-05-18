# -*- coding:utf-8 -*-

import map_reduce

def map_function(data):
	for d in data:
		f = d.rstrip("\r\n").split("\t")
		map_reduce.map_output(f[0], [f[1], f[2]])
	