fp = open("purchase_log")

buy_num = {}
for line in fp:
	f = line.rstrip("\r\n").split("\t")
	user_id = f[0]
	item_id = f[1]
	date = f[2]
	if item_id == "3":
		if user_id not in buy_num:
			buy_num[user_id] = 0
		buy_num[user_id] = buy_num[user_id] + 1
		
for key in buy_num:
	print key + "\t" + str(buy_num[key])