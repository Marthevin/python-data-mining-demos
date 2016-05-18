import sys
import numpy as np
from sklearn import linear_model
from sklearn.decomposition import PCA
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

for dim in xrange(1, 15):
    pca = PCA(n_components = dim)
    pca_x = pca.fit_transform(train_x)

    clf = linear_model.LinearRegression(fit_intercept = True, normalize = True)
    clf.fit(pca_x, train_y)

    y_pred = clf.predict(pca_x)
    print "result for dim=[%d]" % dim, np.sqrt(metrics.mean_squared_error(train_y, y_pred))
