import sys
import numpy as np
from sklearn import linear_model
from sklearn import metrics

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x_array = []
y_array = []
fp = open(sys.argv[1])
fp.readline()
for line in fp:
    f = line.rstrip("\r\n").split("\t")
    x_array.append(map(float, f[0:14]))
    y_array.append(float(f[13]))

for i in xrange(0, len(x_array)):
    for j in [1, 3, 8, 9, 12]:
        x_array[i].append(x_array[i][j] * x_array[i][j])
        x_array[i].append(x_array[i][j] * x_array[i][j] * x_array[i][j])

train_x = np.array(x_array[0:-1])
train_y = np.array(y_array[1:])

clf = linear_model.LinearRegression(fit_intercept = True, normalize = True)
clf.fit(train_x[:, [1,3,4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23]], train_y)

y_pred = clf.predict(train_x[:, [1,3,4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23]])

print clf.intercept_
print clf.coef_
print np.sqrt(metrics.mean_squared_error(train_y, y_pred))

r_error = y_pred - train_y

for (i, j) in enumerate([1,3,4,6,7,8,9,11,12,13]):
    p = plt.subplot(2, 5, i + 1)
    if i in [0, 1, 8, 9]:
        p.semilogx(train_x[:, j], r_error, "o")
    else:
        p.plot(train_x[:, j], r_error, "o")

plt.savefig("r_error_vs_feature")
