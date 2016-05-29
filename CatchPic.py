# -*- coding: UTF-8 -*-
import requests
import os
from lxml import etree
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
def downPic(n):
    a = requests.get('http://www.meizitu.com/a/list_1_' + str(n) + '.html',headers=headers)
    selector = etree.HTML(a.text)
    content = selector.xpath('//*[@id="maincontent"]/div[1]/ul/li/div/div/a/@href')
    k = 1
    for each in content:
        print(each)
	try:
		page_content = requests.get(each,headers=headers)
		img_selector = etree.HTML(page_content.text)
		img_urls = img_selector.xpath('//*[@id="picture"]/p/img/@src')
		i = 1
		for url in img_urls:
		    print('Downloading: '+url)
		    try:
		    	img_content = requests.get(url,headers=headers,timeout=10)
		    	fp = open('Pic/' + str(n) + '-' + str(k) + '-' + str(i) + '.jpg', 'wb')
		    	fp.write(img_content.content)
		    	fp.close()
		    except requests.exceptions.Timeout:
			print('TimeOUt :'+ url)
		    i += 1
	except	requests.exceptions.ConnectionError:
		pass
        k += 1

# The main Func
if os.path.exists('Pic'):
	pass
else :
	os.makedirs('Pic')

for j in range(1, 20):
    downPic(j)
