# -*- coding:utf-8 -*-

import math

#用来计算hj的函数
def calc_h(w, x):
	z = 0
	for i in range(len(w)):
		z = z + w[i] * x[i]
		
	return 1 / (1 + math.exp(-z))

#初始化所有w为0
fea_num = 6
w = []
for i in range(fea_num):
	w.append(0.0)
	
#开始循环
iter = 0
for iter in range(0, 100):
	#初始化所有负梯度为0
	ngrad = []
	for i in range(fea_num):
		ngrad.append(0.0)
	#逐条读入样本，累加计算负梯度
	fp = open("train_data")
	for line in fp:
		x = []
		f = line.rstrip("\r\n").split("\t")
		y = int(f[0])
		for i in range(1, len(f)):
			x.append(int(f[i]))
		h = calc_h(w, x)
		for i in range(fea_num):
			ngrad[i] = ngrad[i] + 0.005 * (y - h) * x[i]
			
	#更新参数w
	for i in range(0, fea_num):
		w[i] = w[i] + ngrad[i]
		
for i in range(fea_num):
	print i, w[i]