# coding:utf-8

import urllib2
import json
import city

url_bj = 'http://www.weather.com.cn/data/cityinfo/101010100.html' 


cont_str = urllib2.urlopen(url_bj).read()
cont_json = json.loads(cont_str)
data = cont_json['weatherinfo']
for i in data:
	print '%s:%s' %(i,data[i])
