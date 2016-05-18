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
kb_selector = feature_selection.SelectKBest(feature_selection.chi2, k = 1000)
new_train_x = kb_selector.fit_transform(train_x, train_y)
print len(kb_selector.get_support(True))
precision = cross_validation.cross_val_score(clf, new_train_x, train_y, cv = 5, scoring = "precision")
recall = cross_validation.cross_val_score(clf, new_train_x, train_y, cv = 5, scoring = "recall")
print np.sum(precision) / np.size(precision), np.sum(recall) / np.size(recall)

clf.fit(new_train_x, train_y)
y_pred = clf.predict(new_train_x)
print metrics.precision_score(train_y, y_pred), metrics.recall_score(train_y, y_pred)

feature_names = tokenizer.get_feature_names()
kb_support = kb_selector.get_support(True)
pos_weight = []
neg_weight = []
for i in xrange(len(clf.feature_log_prob_[0])):
    pos_weight.append(clf.feature_log_prob_[0][i] - clf.feature_log_prob_[1][i])
    neg_weight.append(clf.feature_log_prob_[1][i] - clf.feature_log_prob_[0][i])
top10_pos_index = sorted(range(len(pos_weight)), key = lambda k: pos_weight[k], reverse = True)
print "Positive words:"
for i in top10_pos_index[0:10]:
    print feature_names[kb_support[i]], pos_weight[i]
top10_neg_index = sorted(range(len(neg_weight)), key = lambda k: neg_weight[k], reverse = True)
print "Negative words:"
for i in top10_neg_index[0:10]:
    print feature_names[kb_support[i]], neg_weight[i]




