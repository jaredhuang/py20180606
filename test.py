#!/usr/bin/python
# coding:utf8
'''
int  shu zi
float fu dian shu

str  zi fu chuan
    you xu de , bu ke  xiu gai  , yin hao bao wei de dou jiao zi fu chuan

    xu lei  jiu qian chu  suo yin  le

list  shi zi you xu de --->  rang(10)

tuple ----> .conf  .yaml  .py   ---> ()

dict ---->  /usr/local/python/bin/pip install psutil    <--- json

    dir(psutil)  zhan shi  zhge  mo kuai de suo you fang fa

    {"system":"centos","admin":"root"}


----  bian liang ---->

    In [10]: request=("while",'give me money')

    In [11]: name,doing=request

    In [12]: name
    Out[12]: 'while'

    In [13]: doing
    Out[13]: 'give me money'

'''
import urllib2
request=urllib2.Request("http://www.cip.cc/47.89.49.55")
response=urllib2.urlopen(request)
print response.read()

import json
data1 =[1,2,3]
data2 = (1,2,3)
data3 = {"name":"jared",'age':21}
print type(data1)
print type(data2)
print type(data3)

data = [{'a':1,'b':2}]
json=json.dumps(data),sort_keys=True,indent=4,separators=(',',':')
print json

