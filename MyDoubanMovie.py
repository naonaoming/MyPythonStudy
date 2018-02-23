# -*-coding:utf8-*-

import urllib
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import time
import redis
import json
import random

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

proxies = {
    'http': 'http://61.155.164.108:3128',
    'http': 'http://116.199.115.79:80',
    'http': 'http://42.245.252.35:80',
    'http': 'http://106.14.51.145:8118',
    'http': 'http://116.199.115.78:80',
    'http': 'http://123.147.165.143:8080',
    'http': 'http://58.62.86.216:9999',
    'http': 'http://202.201.3.121:3128',
    'http': 'http://119.29.201.134:808',
    'http': 'http://61.155.164.112:3128',
    'http': 'http://123.57.76.102:80',
    'http': 'http://116.199.115.78:80',
}

proxie = {
        'http' : 'http://122.193.14.102:80'
    }

def LoadUserAgents(ua_file):
    usa = []
    with open(ua_file,'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                usa.append(ua.strip()[1:-1 - 1])
    random.shuffle(usa)
    return usa

if __name__ == '__main__':
    r = redis.Redis(host="localhost",port=6379,db=0)
    # print(r.lrange('rate',0,-1))
    # exit(0)
    # r.ltrim('title',1,0)
    # r.ltrim('rate',1,0)
    # print(r.llen('title'))
    # exit(0)
    count = 1
    uas = LoadUserAgents('user_agent.txt')
    head = {'User-Agent':random.choice(uas)}

    while 1:
        time.sleep(np.random.rand() * 10)
        # url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%97%A5%E6%9C%AC&sort=recommend&page_limit=20&page_start=20'
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%97%A5%E6%9C%AC&sort=recommend&page_limit=20&page_start=' + str(
            (count - 1) * 20)
        print(url)
        jscontent = requests.get(url,headers=head,proxies=proxies).text
        #jscontent = jscontent.decode('utf-8')
        print(jscontent)
        try:
            jsDict = json.loads(jscontent)
            #print(jsDict)
            for i in jsDict["subjects"]:
                print(i['title'])
                print(i['rate'])
                r.lpush('rate',i['rate'])
                r.lpush('title',i['title'])
        except ValueError:
            pass
        count += 1
        if count > 15:
            count = 1
