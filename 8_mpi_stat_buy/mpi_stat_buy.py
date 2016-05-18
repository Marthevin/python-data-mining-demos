# -*- coding:utf-8 -*-

import mpi4py.MPI as MPI  
import time

comm = MPI.COMM_WORLD  
comm_rank = comm.Get_rank()  
comm_size = comm.Get_size()  
#rank0-3, Type A机器
if comm_rank < 2:
    if comm_rank == 0:
        fp = open("purchase_log_0")
    if comm_rank == 1:
        fp = open("purchase_log_1")
            
    for line in fp:
        f = line.rstrip("\r\n").split("\t")
        user_id = int(f[0])
        item_id = f[1]
        if item_id == "3":
            dest = user_id % 2 + 2
            comm.send(f, dest = dest)
            print "%s send to %s %s" % (str(comm_rank), str(dest), str(user_id))
            #time.sleep(0.1)

    comm.send(["-1", "-1"], dest = 2)
    comm.send(["-1", "-1"], dest = 3)

#rank4-5, Type B机器
if comm_rank >= 2:
    buy_num = {}
    finish_num = 0
    while True:
        data_recv = comm.recv(source = -2, tag = -1)
        print "%s recv %s" % (str(comm_rank), str(data_recv[0]))
        user_id = data_recv[0]
        if user_id == "-1":
            finish_num += 1
            if finish_num == 2:
                break
            continue
        if user_id not in buy_num:
            buy_num[user_id] = 0
        buy_num[user_id] = buy_num[user_id] + 1

    for user_id in buy_num:
        print user_id, buy_num[user_id]
