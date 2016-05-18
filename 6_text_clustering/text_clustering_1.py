import sys
reload(sys)
sys.setdefaultencoding("utf8")
import os
import numpy as np
from scipy import stats
from sklearn.feature_extraction import text as text_extractor
from sklearn import cluster
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

tokenizer = text_extractor.CountVectorizer(decode_error = "ignore")
count_m = tokenizer.fit_transform(text_content)
print count_m.shape
tfidfizer = text_extractor.TfidfTransformer()
tfidf_m = tfidfizer.fit_transform(count_m)

kmeans_ = cluster.KMeans(n_clusters = 5, max_iter = 300)
y_pred = kmeans_.fit_predict(tfidf_m)
print y_pred


