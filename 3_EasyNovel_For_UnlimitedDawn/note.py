#coding=utf-8

import urllib
from bs4 import BeautifulSoup

base ='http://www.17k.com'
url ='/chapter/641916/11823633.html'
now_url = base + url
while 1:
    temp = 0
    text = urllib.urlopen(now_url).read()
    bs = BeautifulSoup(text,'lxml')
    print bs.select('#readAreaBox > h1')[0].string.strip()
    for i in  bs.find(id='chapterContentWapper'):
        if i.string:
            print i.string
        if i.name=='div':
            break
        temp +=1
        if temp ==10:
            temp_count =raw_input("**"*20)
            print " "
            temp = 0
 
    next_url = bs.select('li:nth-of-type(7)>a')[0].a.get('href')
    now_url =  base+next_url
    temp_break = raw_input('#'*10)
    
