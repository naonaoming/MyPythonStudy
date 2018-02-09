import requests
import urllib
import re
import os
import datetime
import time
import json
from time import sleep
from PIL import Image

def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time(): return int(round(time.time() * 1000))

    return current_milli_time()

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

for i in range(1,1):
    mymid = 9900 + i

    payload = {
        '_': '1518077517787',
        'mid': str(mymid)
    }
    # payload = {
    #     'mid': str(mymid)
    # }

    #print(payload)
    jscontent = requests \
        .session() \
        .post('http://space.bilibili.com/ajax/member/GetInfo',
            headers=head,
            data=payload,
            proxies=proxies) \
        .text

#print(jscontent)
    try:
        jsDict = json.loads(jscontent)
        statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
        if statusJson:
            jsData = jsDict['data']
            name = jsData['name']
            face = jsData['face']
            print(face)
            pngname = 'D:\lest\log' + name + '.png'
            urllib.request.urlretrieve(face,pngname)
    except ValueError:
        print("漏了张图")
        pass

urlinfo = 'http://space.bilibili.com/ajax/member/MyInfo'
mydata = {'vmid':'33929530'}
content = requests.session().post(urlinfo,headers=head,data=mydata,proxies=proxies).text
print(content)
# urlinfo = http://space.bilibili.com/ajax/member/MyInfo?vmid=33929530


url = 'http://www.runoob.com/design-pattern/factory-pattern.html'
