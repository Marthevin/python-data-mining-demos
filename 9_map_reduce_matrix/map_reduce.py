# -*- coding:utf-8 -*-

map_output_buffer = []
reduce_output_buffer = []

#�ṩ��mapper����ӿ�
def map_output(key, value):
	map_output_buffer.append([key, value])
	
def reduce_output(key, value):
	reduce_output_buffer.append([key, value])