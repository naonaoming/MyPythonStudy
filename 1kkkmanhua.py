import urllib
import requests
from bs4 import BeautifulSoup
import os
import random
import logging

def LoadUserAgents(ua_file):
    usa = []
    with open(ua_file,'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                usa.append(ua.strip()[1:-1 - 1])
    random.shuffle(usa)
    return usa

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

uas = LoadUserAgents('user_agent.txt')
ua = random.choice(uas)
head = {
    'Referer':'http://www.1kkk.com/ch1-117459-p5/',
    'Host':'manhua1021-61-174-50-98.cdndm5.com',
    'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection':'keep-alive',
    'User-Agent':ua
}

# def use_logging(func):
#     def mywrapper(*args,**kwargs):
#         #logging.warn("%s is running" % func.__name__)
#         print("%s is running" % func.__name__)
#         return func(*args)
#     return mywrapper
#
# @use_logging
# def foo():
#     print('im foo')

payload={
    'cid':117459,
    'key':'5d13b5dce172d40bab3f5a0e0d6c917e'
}

url = 'http://manhua1021-61-174-50-98.cdndm5.com/11/10684/117459/1_7207.jpg?cid=117459&key=5d13b5dce172d40bab3f5a0e0d6c917e'
url = 'http://ac.tc.qq.com/store_file_download?buid=15017&uin=1422306610&dir_path=/&name=27_05_10_04fbd53f43847f345b93a937994be031_1922.ori'
#url = 'http://manhua1021-61-174-50-98.cdndm5.com/11/10684/117459/3_6805.png?cid=117459&key=5ed1a1d0953ccdd8a32ecd4ffb4e05e0'
#url = 'http://manhua1021-61-174-50-98.cdndm5.com/11/10684/117459/5_3709.png?cid=117459&key=5d13b5dce172d40bab3f5a0e0d6c917e'
r = requests.get(url,headers=head)
path = 'D:\pic\R100.png'
with open(path,'wb') as f:
    f.write(r.content)

print(r)