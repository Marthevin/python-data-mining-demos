# -*- coding:utf-8 -*-

import sys
import getopt
import mapper
import reducer
import map_reduce

#将文件拆成map_num份，作为每个mapper的输入
def split_file(map_num, input_file_name):
	fp = open(input_file_name)
	blocks = []
	for i in range(0, map_num):
		blocks.append([])
	lines = []
	for line in fp:
		lines.append(line)
	num_per_map = int(float(len(lines)) / map_num + 1)
	for (i, line) in enumerate(lines):
		map_i = i / num_per_map
		blocks[map_i].append(line)
		
	return blocks


#map-reduce主控函数
def mr_main(map_num, reduce_num, input_file_name):
	#拆分大文件为block
	blocks = split_file(map_num, input_file_name)
	
	#将每个block送给每个mapper使用
	for i in range(0, map_num):
		print "Schedule mapper", i, "to run!"
		mapper.map_function(blocks[i])
		
	#将mapper的输出用key做hash，分桶，生成每个reducer的输入
	reduce_input = []
	for i in range(reduce_num):
		reduce_input.append([])
	for r in map_reduce.map_output_buffer:
		key = r[0]
		value = r[1]
		reduce_id = hash(key) % reduce_num
		reduce_input[reduce_id].append([key, value])

	#将数据送给每个reducer
	for i in range(0, reduce_num):
		print "Schedule reducer", i, "to run!"
		reducer.reduce_function(reduce_input[i])
		#将reducer的输出写入文件
		fp = open("part.0000" + str(i), "w")
		for r in map_reduce.reduce_output_buffer:
			print >> fp, str(r[0]) + "\t" + str(r[1])
		map_reduce.reduce_output_buffer = []
			
options,args = getopt.getopt(sys.argv[1:], "hm:r:f:", ["help", "map_num=", "reduce_num=", "input_file="])
for name, value in options:
	if name in ("-h", "--help"):
		print "Usage: python map_reduce_main.py --map_num=5 --reduce_num=2 --input_file=xxx.txt"
		exit(0)
	elif name in ("-m", "--map_num"):
		map_num = int(value)
	elif name in ("-r", "--reduce_num"):
		reduce_num = int(value)
	elif name in ("-f", "--input_file"):
		input_file = value
	
mr_main(map_num, reduce_num, input_file)
		