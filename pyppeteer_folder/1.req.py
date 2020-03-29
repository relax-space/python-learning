"""
无法爬取JavaScript渲染页面之后的内容
python.exe .\pyppeteer_folder\1.req.py
"""

import requests
from pyquery import PyQuery as pq
 
url = 'http://quotes.toscrape.com/js/'
response = requests.get(url)
doc = pq(response.text)
print('Quotes:', doc('.quote').length)