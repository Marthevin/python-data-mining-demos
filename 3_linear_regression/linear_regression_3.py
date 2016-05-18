import sys
import numpy as np
from sklearn import linear_model
from sklearn import metrics

x_array = []
y_array = []
fp = open(sys.argv[1])
fp.readline()
for line in fp:
    f = line.rstrip("\r\n").split("\t")
    x_array.append(map(float, f[0:14]))
    y_array.append(float(f[13]))

train_x = np.array(x_array[0:-1])
train_y = np.array(y_array[1:])

clf = linear_model.LinearRegression(fit_intercept = True, normalize = True)
clf.fit(train_x[:, [1,3,4,6,7,8,9,11,12,13]], train_y)

y_pred = clf.predict(train_x[:, [1,3,4,6,7,8,9,11,12,13]])

print clf.intercept_
print clf.coef_
print np.sqrt(metrics.mean_squared_error(train_y, y_pred))
