# -*- coding:utf-8 -*-

import map_reduce

def reduce_function(data):
	buy_num = {}
	for d in data:
		user_id = d[0]
		if user_id not in buy_num:
			buy_num[user_id] = 0
		buy_num[user_id] = buy_num[user_id] + 1
		
	for user_id in buy_num:
		map_reduce.reduce_output(user_id, str(buy_num[user_id]))