import numpy as np
import pandas as pd
import os
import urllib
import requests
import re
import random

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

head = {
    'Referer':'http://www.dianping.com/shanghai/ch10/g110p50?aid=72351070%2C93077944%2C97435241%2C98281287&cpt=72351070%2C93077944%2C97435241%2C98281287&tc=1',
    'Host':'www.dianping.com',
    'Date':'Wed, 07 Mar 2018 06:55:43 GMT',
    'Content-Type':'text/html;charset=UTF-8',
    'Upgrade-Insecure-Requests':'1'
}

uas = LoadUserAgents('user_agent.txt')
head['User-Agent'] = random.choice(uas)
#head['Referer'] = 'http://www.dianping.com'

#url = 'http://www.dianping.com/shanghai/ch10/g110'
url = 'http://www.dianping.com/shanghai/ch10/g110p50?aid=72351070%2C93077944%2C97435241%2C98281287&cpt=72351070%2C93077944%2C97435241%2C98281287&tc=1'
#url = 'http://www.dianping.com'
hosturl = 'http://www.dianping.com'

r1 = requests.get(hosturl,headers=head)
# page1 = r.content.decode('utf-8')
r2 = requests.get(url,headers=head)
page2 = r2.content.decode('utf-8')

print('asd123')


