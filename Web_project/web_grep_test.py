#! usr/bin/env python
import requests
import matplotlib.pyplot as plt

url = 'http://1.15.140.205/' # srtp server created by wxf
try:
    print('开始运行')
    str_html = requests.get(url)
    str_html.encoding = str_html.apparent_encoding
    str_data = str_html.text
    print('数据成功爬取')

except:
    print(Exception)

print(str_data)