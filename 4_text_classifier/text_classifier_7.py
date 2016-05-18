# -*- coding:utf-8 -*-

import sys
import re
import jieba
reload(sys)
sys.setdefaultencoding("utf-8")
import numpy as np
from sklearn import linear_model
from sklearn import grid_search

def load_region(file_name):
    region = {}
    for line in open(file_name):
        f = line.rstrip("\r\n").split("\t")
        if f[0] == "id":
            continue
        if len(f) > 1:
            region[f[1].decode("utf8")] = 1
            region[f[1].decode("utf8").rstrip("省市区")] = 1
	
    return region

def load_content(file_name):
    content_dict = []
    fp = open(file_name)
    for line in fp:
        f = line.rstrip("\r\n").split("\t")        
        content = "\t".join(f[2:]).rstrip("\t ").lstrip("\t ")
        terms = []
        for t in jieba.cut(content.decode("utf8"), cut_all=False):
            terms.append(t)
        uniq_term = {}
        for t in terms:
            if t in [u",", u".", u"!", u"?", u":", u";", u"，", u"。", u"！", u"？", u"：", u"；"]:
                continue
            if t not in uniq_term:
                uniq_term[t] = 0
            uniq_term[t] += 1
        content_dict.append(uniq_term)
    return content_dict

def get_feature(u_str, region_dict, content):
    terms = []
    for t in jieba.cut(u_str, cut_all=False):
        terms.append(t)
    features = []
    features.append(get_region_feature(terms, region_dict))
    features.append(get_letters_feature(u_str))
    features.append(get_kw_feature(u_str))
    f4 = get_content_feature(terms, content)
    features.extend(f4)
    if (f4[1] > 0.5 or f4[0] * 20 > 0.5) and features[1] > 0.99:
        features[1] = 0

    return features
	
def get_region_feature(terms, region_dict):
    for w in terms:
        if w in region_dict:
            return 1

    return 0
			
def get_letters_feature(u_str):
    letter_num = 0
    for c in u_str:
        if re.match(u"[\u4e00-\u9faf]+", c) == None:
            letter_num += 1
    return float(letter_num) / len(u_str)
	
def get_kw_feature(u_str):
    if u"编号" in u_str or u"招" in u_str or u"聘" in u_str or u"薪" in u_str or u"福" in u_str:
        return 1
    else:
        return 0
		
def get_content_feature(terms, content):
    hit_num = 0
    for t in terms:
        if t in content:
            hit_num += content[t]			

    f = [0, 0]
    if hit_num < 20:
        hit = hit_num / float(10)
        if hit > 1:
            hit = 1
        f[0] = hit
    else:
        f[1] = 1
    
    return f

region_dict = load_region("region.txt")
content_dict = load_content(sys.argv[1])
fp = open(sys.argv[1])
x_array = []
y_array = []
line_no = 0
for line in fp:
    f = line.rstrip("\r\n").split("\t")
    y_array.append(int(f[0]))
    x_array.append(get_feature(f[1].decode("utf8"), region_dict, content_dict[line_no]))
    line_no += 1

train_x = np.array(x_array)
train_y = np.array(y_array)
lr = linear_model.LogisticRegression()
penalty_c = []
for i in xrange(1, 21):
    penalty_c.append(i / 10.0)
h_param = {"C":penalty_c, "penalty":["l1", "l2"], "solver":["liblinear"]}
clf = grid_search.GridSearchCV(lr, h_param, scoring = "f1")
clf.fit(train_x, train_y)
print clf.best_score_
print clf.best_params_
