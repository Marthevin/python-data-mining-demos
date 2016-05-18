import mpi4py.MPI as MPI  

comm = MPI.COMM_WORLD  
comm_rank = comm.Get_rank()  
comm_size = comm.Get_size()  

# point to point communication  
data_send = [comm_rank, comm_rank]

dest = comm_rank + 1
if dest >= comm_size:
    dest = 0
comm.send(data_send,dest = dest)

source = comm_rank - 1
if source < 0:
    source = comm_size - 1
data_recv =comm.recv(source = source)

print "my rank is", comm_rank, "and Ireceived:", data_recv
