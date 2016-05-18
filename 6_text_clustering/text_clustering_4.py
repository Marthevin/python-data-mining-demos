import sys
reload(sys)
sys.setdefaultencoding("utf8")
import os
import numpy as np
from scipy import stats
from sklearn.feature_extraction import text as text_extractor
from sklearn import cluster
from sklearn import metrics
import jieba
from sklearn.decomposition import PCA
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import random

class_ = ["Art", "Computer", "Medical", "Military", "Sports"]
labels = []
text_content = []
for (i, c) in enumerate(class_):
    file_num = 0
    for f in os.listdir("answer/" + c):
        try:
            content = open("answer/" + c + "/" + f).read().decode("gbk").encode("utf8")
        except:
            try:
                content = open("answer/" + c + "/" + f).read().decode("utf8").encode("utf8")
            except:
                content = open("answer/" + c + "/" + f).read()
        terms_list = jieba.cut(content, cut_all = False)
        text_content.append("\t".join(terms_list))
        labels.append(i)
        file_num += 1
        if file_num > 70:
            break
y_true = np.array(labels)

tokenizer = text_extractor.CountVectorizer(decode_error = "ignore")
count_m = tokenizer.fit_transform(text_content)
print count_m.shape
tfidfizer = text_extractor.TfidfTransformer()
tfidf_m = tfidfizer.fit_transform(count_m)

kmeans_ = cluster.KMeans(n_clusters = 5, max_iter = 300)
y_pred = kmeans_.fit_predict(tfidf_m)
distance_m = kmeans_.fit_transform(tfidf_m)

pca = PCA(n_components = 2)
pca_m = pca.fit_transform(distance_m)

colors = ["r", "b", "g", "y", "c"]
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
sampled = random.sample(range(0, np.size(y_true)), np.size(y_true))
for i in sampled:
    ax.plot(pca_m[i, 0], pca_m[i, 1], "o", markerfacecolor = colors[y_true[i]], markeredgecolor = "k")

ax = fig.add_subplot(1, 2, 2)
for i in sampled:
    ax.plot(pca_m[i, 0], pca_m[i, 1], "o", markerfacecolor = colors[y_pred[i]], markeredgecolor = "k")

plt.savefig("cl")
