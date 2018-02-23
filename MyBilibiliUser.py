import numpy as np
import urllib
import requests
import re
import redis
import time
import json
import sys
from imp import reload
import random
import datetime
from multiprocessing.dummy import Pool as ThreadPool
import threading

reload(sys)

def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time(): return int(round(time.time() * 1000))

    return current_milli_time()

def LoadUserAgents(ua_file):
    usa = []
    with open(ua_file,'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                usa.append(ua.strip()[1:-1 - 1])
    random.shuffle(usa)
    return usa

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

proxies = {
    'http': 'http://61.155.164.108:3128',
    'http': 'http://116.199.115.79:80',
    'http': 'http://42.245.252.35:80',
    'http': 'http://106.14.51.145:8118',
    'http': 'http://123.147.165.143:8080',
    'http': 'http://58.62.86.216:9999',
    'http': 'http://202.201.3.121:3128',
    'http': 'http://119.29.201.134:808',
    'http': 'http://61.155.164.112:3128',
    'http': 'http://123.57.76.102:80',
}

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/45388',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}

def getsource(url):
    # url = 'https://space.bilibili.com/' + str(i)
    print(url)
    payload = {
        '_': datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
        'mid': url.replace('https://space.bilibili.com/', '')
    }
    ua = random.choice(uas) #随机UA
    head = {
        'User-Agent':ua,
        'Referer': 'https://space.bilibili.com/' + str(i) + '?from=search&seid=' + str(random.randint(10000, 50000))
    }
    response_data = requests.session().post('http://space.bilibili.com/ajax/member/GetInfo',headers=head,data=payload,proxies=proxies).text
    # print(jsDict)
    try:
        jsDict = json.loads(response_data)
        json_status = jsDict['status'] if 'status' in jsDict.keys() else False
        if json_status == True:
            if 'data' in jsDict.keys():
                data = jsDict['data']
                mid = data['mid']
                name = data['name']
                sex = data['sex']
                if len(sex) < 2:
                    sex = 'undefined'
                rank = data['rank']
                r.lpush('mid',mid)
                r.lpush('name',name)
                r.lpush('sex',sex)
                print("succeed")
                print(mid)
    except:
        pass

class myThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self):
        getsource(self.url)

r = redis.Redis(host="localhost",port=6379,db=1)
uas = LoadUserAgents('user_agent.txt')

for m in range(99,10100):
    urls = []
    for i in range(m * 100, (m + 1) * 100):
        url = 'https://space.bilibili.com/' + str(i)
        urls.append(url)
        thread1 = myThread(url)
        thread1.start()
       # thread1.join()
       # print("success")
        # getsource(url)

    # pool = ThreadPool(1)
    # try:
    #     results = pool.map(getsource,urls)
    # except:
    #     print("connect error")
    #     pool.close()
    #     pool.join()
    #     time.sleep(11)
    #     pool = ThreadPool(1)
    #     results = pool.map(getsource, urls)

    time.sleep(30)

    # break