import requests
import re
from bs4 import BeautifulSoup
s = requests.session()
post_data = {
    "origURL":"/home.do",
    "lbskey":"1452526627910CYWmy6cynKyULVwuSg7K",
    "c":"",
    "pq":"",
    "appid":"",
    "ref":"http://m.renren.com/q.do?null",
    "email":"xxxxxx@gmail.com",
    "password":"xxxxxx"
}
s.post("http://3g.renren.com/login.do?autoLogin=true&&fx=0")
r = s.get("http://3g.renren.com/home.do?sid=LIJty1DTUyl8jH897IA0IK&bm=238010984_17de7bed76027b8da98f3483ebeb7355_1452526654031&f=1&w=1&")
#r = s.get("http://www.renren.com/238010984")
soup = BeautifulSoup(r.content)

for l in soup.body.find("div", class_="list").contents:
    print l, "\r\n"


