#!/usr/bin/env python
import requests
import re
#html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
#html = requests.get('http://jp.tingroom.com/yuedu/yd300p/',headers = headers)
html = requests.get('http://www.jikexueyuan.com',headers = headers)
# print html.text
title = re.findall('<p class="skuTitle">(.*?)</p>',html.text,re.S)
for each in title:
	print each

