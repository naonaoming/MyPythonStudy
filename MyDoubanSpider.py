# -*-coding:utf8-*-

import sys
import imp
from imp import reload
import requests
import urllib
import re
import numpy as np
import time
from bs4 import BeautifulSoup
import jieba
import redis

reload(sys)

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

if __name__ == '__main__':
    r = redis.Redis(host='localhost',port=6379,db=0)

    book_tag = '小说'
    page_num = 1
    while 1:
        url = 'http://www.douban.com/tag/' + urllib.request.quote(book_tag) + '/book?start=' + str(page_num * 15)
        print(url)
        time.sleep(np.random.rand() * 5)
        try:
            req = urllib.request.Request(url,headers=hds[page_num%len(hds)])
            text = urllib.request.urlopen(req).read()
            text = text.decode('utf-8') # 编码改为utf-8，没找到修改默认编码的方法
            soup = BeautifulSoup(text,"html.parser")
            list_soup = soup.find('div',{'class': 'mod book-list'})
            #words = jieba.cut(list_soup)
            for book_info in list_soup.findAll('dd'):
                title=book_info.find('a',{'class','title'}).string.strip()
                desc_list=book_info.find('div',{'class','desc'})    # 翻译？/作者/出版社/时间/价格
                #print(desc_list)
                print(title)
            page_num += 1
        except Exception(e):
            print(e)
        page_num += 1
    #print(urllib.request.quote(book_tag))
