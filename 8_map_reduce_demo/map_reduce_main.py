# -*- coding:utf-8 -*-

import sys
import getopt
import mapper
import reducer
import map_reduce

#���ļ����map_num�ݣ���Ϊÿ��mapper������
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


#map-reduce���غ���
def mr_main(map_num, reduce_num, input_file_name):
	#��ִ��ļ�Ϊblock
	blocks = split_file(map_num, input_file_name)
	
	#��ÿ��block�͸�ÿ��mapperʹ��
	for i in range(0, map_num):
		print "Schedule mapper", i, "to run!"
		mapper.map_function(blocks[i])
		
	#��mapper�������key��hash����Ͱ������ÿ��reducer������
	reduce_input = []
	for i in range(reduce_num):
		reduce_input.append([])
	for r in map_reduce.map_output_buffer:
		key = r[0]
		value = r[1]
		reduce_id = hash(key) % reduce_num
		reduce_input[reduce_id].append([key, value])

	#�������͸�ÿ��reducer
	for i in range(0, reduce_num):
		print "Schedule reducer", i, "to run!"
		reducer.reduce_function(reduce_input[i])
		#��reducer�����д���ļ�
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
		