# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

proxies = {"http":"http://120.52.73.36:8080"}
r = requests.get("http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=hello", proxies = proxies)
soup = BeautifulSoup(r.content)

print r.content

result_div = soup.find_all(name="div", class_=re.compile(".*c-container.*"))

for div in result_div:
    r = requests.get(div.h3.a.attrs["href"])
    print r.url


