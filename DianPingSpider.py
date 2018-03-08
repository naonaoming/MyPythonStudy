import numpy as np
import pandas as pd
import os
import urllib
import requests
import re
import random
from bs4 import BeautifulSoup
import json

# list = [22711693,24759450,69761921,69761921,22743334,66125712,22743270,57496584,75153221,57641884,66061653,70669333,57279088,24740739,66126129,
#         75100027,92667587,92452007,72345827,90004047,90485109,90546031,83527455,91070982,83527745,94273474,80246564,83497073,69027373,96191554,
#         96683472,90500524,92454863,92272204,70443082,96076068,91656438,75633029,96571687,97659144,69253863,98279207,90435377,70669359,96403354,
#         83618952,81265224,77365611,74592526,90479676,56540304,37924067,27496773,56540319,32571869,43611843,58612870,22743340,67293664,67292945,
#         57641749,75157068,58934198,75156610,59081304,75156647,75156702,67293838,]
# returnList = []
# proxies = {
#     # "https": "http://14.215.177.73:80",
#     "http": "http://202.108.2.42:80",
# }
# headers = {
#     'Host': 'www.dianping.com',
#     'Referer': 'http://www.dianping.com/shop/22711693',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/535.19',
#     'Accept-Encoding': 'gzip'
# }
# cookies = {
#     '_lxsdk_cuid': '16146a366a7c8-08cd0a57dad51b-32637402-fa000-16146a366a7c8',
#     'lxsdk': '16146a366a7c8-08cd0a57dad51b-32637402-fa000-16146a366a7c8',
#     '_hc.v': 'ec20d90c-0104-0677-bf24-391bdf00e2d4.1517308569',
#     's_ViewType': '10',
#     'cy': '16',
#     'cye': 'wuhan',
#     '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
#     '_lxsdk_s': '1614abc132e-f84-b9c-2bc%7C%7C34'
#
# }
# requests.adapters.DEFAULT_RETRIES = 5
# s = requests.session()
# s.keep_alive = False
# for i in list:
#     url = "https://www.dianping.com/shop/%s/review_all" % i
#     r = requests.get(url, headers=headers, cookies=cookies,proxies = proxies)
#     # print r.text
#     soup = BeautifulSoup(r.text, 'lxml')
#
#     lenth = soup.find_all(class_='PageLink').__len__() + 1
#     #print lenth
#     for j in range(lenth):
#         urlIn = "http://www.dianping.com/shop/%s/review_all/p%s" % (i, j)
#         re = requests.get(urlIn, headers=headers, cookies=cookies,proxies =proxies)
#         soupIn = BeautifulSoup(re.text, 'lxml')
#         title = soupIn.title.string[0:15]
#         #print title
#         coment = []
#         coment = soupIn.select('.reviews-items li')
#
#         for one in coment:
#             try:
#                 if one['class'][0]=='item':
#                     continue
#             except:
#                 pass
#             name = one.select_one('.main-review .dper-info .name')
#             #print name.get_text().strip()
#             name = name.get_text().strip()
#             star = one.select_one('.main-review .review-rank span')
#             #print star['class'][1][7:8]
#             star = star['class'][1][7:8]
#             pl = one.select_one('.main-review .review-words')
#             pl['class'] = {'review-words'}
#             words = pl.get_text().strip()
#             returnList.append([title,name,star,words])
#
# file = open("/Users/huojian/Desktop/store_shop.sql","w")
# for one in returnList:
#     file.write("\n")
#     file.write(unicode(one[0]))
#     file.write("\n")
#     file.write(unicode(one[1]))
#     file.write("\n")
#     file.write(unicode(one[2]))
#     file.write("\n")
#     file.write(unicode(one[3]))
#     file.write("\n")
#
# exit(1)

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
    'Referer':'http://www.dianping.com/',
    'Host':'www.dianping.com',
    'Content-Type':'text/html;charset=UTF-8',
    'Upgrade-Insecure-Requests':'1',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding':'gzip, deflate',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cookie':'cy=1; cye=shanghai; _lxsdk_cuid=161ff24f723c8-0674058f08990d-b353461-144000-161ff24f724c8; _lxsdk=161ff24f723c8-0674058f08990d-b353461-144000-161ff24f724c8; _hc.v=041fc5ff-1c43-e2d6-279f-29ad5a82e4fd.1520404068; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16205098c1d-63f-8d7-26a%7C%7C51'
}
#cy=1; cye=shanghai; _lxsdk_cuid=161ff24f723c8-0674058f08990d-b353461-144000-161ff24f724c8; _lxsdk=161ff24f723c8-0674058f08990d-b353461-144000-161ff24f724c8; _hc.v=041fc5ff-1c43-e2d6-279f-29ad5a82e4fd.1520404068; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16205098c1d-63f-8d7-26a%7C%7C19
#cy=1; cye=shanghai; _lxsdk_cuid=161ff24f723c8-0674058f08990d-b353461-144000-161ff24f724c8; _lxsdk=161ff24f723c8-0674058f08990d-b353461-144000-161ff24f724c8; _hc.v=041fc5ff-1c43-e2d6-279f-29ad5a82e4fd.1520404068; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16205098c1d-63f-8d7-26a%7C%7C27

uas = LoadUserAgents('user_agent.txt')
head['User-Agent'] = random.choice(uas)
#head['Referer'] = 'http://www.dianping.com'

url = 'http://www.dianping.com/shanghai/ch10/g110'
#url = 'http://www.dianping.com/shanghai/ch10/g110p50?aid=72351070%2C93077944%2C97435241%2C98281287&cpt=72351070%2C93077944%2C97435241%2C98281287&tc=1'
#url = 'http://www.dianping.com'
hosturl = 'http://www.dianping.com'

r1 = requests.get(hosturl,headers=head)
# page1 = r.content.decode('utf-8')
r2 = requests.get(url,headers=head)
page2 = r2.content.decode('utf-8')

soup = BeautifulSoup(page2,'html.parser')
content_wrap = soup.find('div',{'class':'content-wrap'})
all_res = content_wrap.findAll('li')

print('asd123')


