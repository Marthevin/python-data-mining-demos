import sys
import numpy as np
from scipy import stats

x_array = []
y_array = []
fp = open(sys.argv[1])
fp.readline()
for line in fp:
    f = line.rstrip("\r\n").split("\t")
    x_array.append(map(float, f[0:13]))
    y_array.append(float(f[13]))

train_x = np.array(x_array[0:-1])
train_y = np.array(y_array[1:])

for i in xrange(0, len(x_array[0])):
    print stats.pearsonr(train_x[:, i], train_y)[0]

print stats.pearsonr(train_y[0:-1], train_y[1:])[0]
