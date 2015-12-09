import requests
from lxml import etree

a = requests.get("http://www.wetu.me/search/nature%20outdoor")

selector = etree.HTML(a.text)

content = selector.xpath('//*[@id="gallery-list"]/li/a/img/@data-original')

i = 1
for each in content:
    print('downloading:' + each)
    pic = requests.get(each)
    fp = open('/Users/1akang/Desktop/pictures/' + str(i) + '.jpg', 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1
