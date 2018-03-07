# -*-coding:utf8-*-
import os
import urllib
import sys
from imp import reload
import requests
from bs4 import BeautifulSoup
import random
import base64
import re

reload(sys)

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
head = {
    'Referer':'http://www.iimanhua.com/imanhua/9202/261856.html?p=1',
    'Content-Length':'44846',
    'Content-Type':'image/jpeg',
    'Last-Modified':'Mon, 11 Apr 2016 12:35:13 GMT'
}

head = {'User-Agent':random.choice(uas)}

url = 'http://www.iimanhua.com/imanhua/9202/261857.html?p=1'
url = 'http://www.1kkk.com/ch1-117459/#ipg1'
url = 'http://ac.qq.com/ComicView/chapter/id/530132/cid/3'

r = requests.get(url,headers=head)
# path = 'D:\pic\esd.png'
# with open(path,'wb') as f:
#    f.write(r.content)
content = r.content

#page = content.decode('gb2312')
page = content.decode('utf-8')
idx = page.index('qTcms_S_m_murl_e') if 'qTcms_S_m_murl_e' in page else exit(1)
idx1 = page.index('"', idx)
idx2 = page.index('"', idx1 + 1)
pic64 = page[idx1: idx2]
picurl = base64.b64decode(pic64)
#print(str(picurl))
mystr = picurl.decode('utf-8')
count = 0
for i in mystr.split('$qingtiandy$'):
    purl = 'http://www.iimanhua.com/' + i
    #path = os.path.join('D','pic',i)
    path = 'D:\pic\\' + str(count) + '.png'
    pic_r = requests.get(purl,headers=head)
    with open(path, 'wb') as f:
        f.write(pic_r.content)
        print("success")
        count += 1

#for i in (str(picurl)).split('$qingtiandy$'):
#    print(i)

exit(1)
print(idx)
#if 'qTcms_S_m_murl_e' in page:

    #print('get')
    #exit(1)
soup = BeautifulSoup(content,"html.parser")
myscript = soup.findAll('script')
for i in myscript:
    #if 'qTcms_S_m_murl_e' in i.content:
    #    print("zhejiusle")
    print(i)
list_soup = soup.find('table',{'class':'tbCenter'})

for mytd in list_soup.findAll('td'):
    print(mytd)
    myimg = mytd.find('img')
    mysrc = myimg.attrs['src']
    print(myimg.attrs['src'])

print('abc')
# list_soup = soup.find('div',{'class': 'mod book-list'})

#page = page.decode('utf-8')
# print(page)