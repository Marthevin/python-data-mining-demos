import sys
reload(sys)
sys.setdefaultencoding("utf8")
import os
import numpy as np
#from scipy import stats
from sklearn.feature_extraction import text as text_extractor
from sklearn import cluster
from sklearn import decomposition
from sklearn import metrics
import jieba

class_ = ["Art", "Computer", "Medical", "Military", "Sports"]
labels = []
text_content = []
for (i, c) in enumerate(class_):
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
y_true = np.array(labels)

tokenizer = text_extractor.CountVectorizer(decode_error = "ignore")
count_m = tokenizer.fit_transform(text_content)
print count_m.shape

lda = decomposition.LatentDirichletAllocation(n_topics = 200)
new_train_x = lda.fit_transform(count_m)
print new_train_x.shape

kmeans_ = cluster.KMeans(n_clusters = 5, max_iter = 300)
y_pred = kmeans_.fit_predict(new_train_x)

print metrics.adjusted_rand_score(y_true, y_pred)



