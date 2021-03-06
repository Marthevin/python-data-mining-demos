import numpy as np
from sklearn import linear_model

x_array = []
y_array = []
fp = open("rain.txt","rb")
fp.readline()
for line in fp:
    print line
    f = line.rstrip("\r\n").split("\t")
    x_array.append(map(float, f[0:14]))
    y_array.append(float(f[13]))

train_x = np.array(x_array[0:-1])
train_y = np.array(y_array[1:])

clf = linear_model.LinearRegression(fit_intercept = True, normalize = True)
clf.fit(train_x, train_y)
print clf.intercept_
print clf.coef_
