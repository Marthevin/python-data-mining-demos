import sys
reload(sys)
sys.setdefaultencoding("utf8")
import os
import numpy as np
from sklearn.feature_extraction import text as text_extractor
from sklearn import naive_bayes
from sklearn import feature_selection
from sklearn import cross_validation
from sklearn import metrics

class_ = ["pos", "neg"]

labels = []
text_content = []
for (i, c) in enumerate(class_):
    for f in os.listdir("./" + c):
        content = open("./" + c + "/" + f).read()
        text_content.append(content)
        labels.append(i)
train_y = np.array(labels)

tokenizer = text_extractor.CountVectorizer(decode_error = "ignore")
count_m = tokenizer.fit_transform(text_content)
print count_m.shape
tfidfizer = text_extractor.TfidfTransformer()
tfidf_m = tfidfizer.fit_transform(count_m)

clf = naive_bayes.MultinomialNB()
train_x = tfidf_m
new_train_x = feature_selection.SelectKBest(feature_selection.chi2, k = 1000).fit_transform(train_x, train_y)
precision = cross_validation.cross_val_score(clf, new_train_x, train_y, cv = 5, scoring = "precision")
recall = cross_validation.cross_val_score(clf, new_train_x, train_y, cv = 5, scoring = "recall")
print np.sum(precision) / np.size(precision), np.sum(recall) / np.size(recall)

clf.fit(new_train_x, train_y)
y_pred = clf.predict(new_train_x)
print metrics.precision_score(train_y, y_pred), metrics.recall_score(train_y, y_pred)



