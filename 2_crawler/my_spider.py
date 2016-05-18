# -*- coding:utf-8 -*-

import bs4
from bs4 import BeautifulSoup
import sys
import requests
import time
import re

class Downloader():
    def __init__(self):
        pass

    def get_file_name(self, url):
        f = url.split("?")
        if len(f) > 1:
            new_url = f[0]
        else:
            new_url = url

        p = re.compile(".+://(?P<url>.+)")
        match = re.search(p, new_url)
        if match:
            new_url = match.group("url")

        f = new_url.split("/") 
        if len(f) == 1:
            return new_url + "_dir.html"
        if f[-1] == "":
            filename = f[-2] + "_dir.html"
        else:
            filename = f[-1]
		
        if len(filename.split(".")) != 1 and (not filename.endswith(".html")) and (not filename.endswith(".htm")):
            return None
		
        if (not filename.endswith(".html")) and (not filename.endswith(".htm")):
            filename += ".html"
    
        return filename
	

    def download(self, url):
        retry_num = 0
        download_succ = False
        while retry_num < 3:
            try:
                r = requests.get(url)
                content = r.content
                download_succ = True
                break
            except:
                time.sleep(5)
                retry_num += 1
	
        if not download_succ:
            return []

        file_name = self.get_file_name(url)
        if file_name == None:
            return []
		
        fp = open(file_name, "w")
        print >> fp, content
	
        soup = BeautifulSoup(content)
        if soup == None or soup.body == None:
            return []
        links = []
        for c in soup.body.descendants:
            if isinstance(c, bs4.element.NavigableString):
                continue
            if "href" in c.attrs:
                if c.attrs["href"].find("pcpop.com") != -1:
                    links.append(c.attrs["href"])
			
        return links

class Scheduler():
    def __init__(self):
        self.all_urls_for_crawl = []
        self.crawl_num = 0

    def url_exists(self, url):
        for u in self.all_urls_for_crawl:
            if url.rstrip("/") == u.rstrip("/"):
                return True

        return False

    def push_url(self, url):
        if not self.url_exists(url):
            print "add:", url
            self.all_urls_for_crawl.append(url)

    def pop_url(self):
        if self.crawl_num >= len(self.all_urls_for_crawl):
            return None
        ret = self.all_urls_for_crawl[self.crawl_num]
        self.crawl_num += 1
        return ret

downloader = Downloader()
scheduler = Scheduler()
scheduler.push_url(sys.argv[1])

while True:
    next_url = scheduler.pop_url()
    print next_url
    if next_url == None:
        break

    out_links = downloader.download(next_url)
    print "sleep 5s"
    time.sleep(5) #防止被封
    for url in out_links:
        scheduler.push_url(url)
