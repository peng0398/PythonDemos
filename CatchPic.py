import requests
from lxml import etree

def downPic(n):
    i = 1
    a = requests.get("http://www.wetu.me/search?keyword=city%20view&pageindex="+str(n))
    selector = etree.HTML(a.text)
    content = selector.xpath('//*[@id="gallery-list"]/li/a/img/@data-original')
    for each in content:
        print('downloading:' + each)
        pic = requests.get(each)
        fp = open('/Users/1akang/Desktop/pictures/city' + str(n)+'-'+str(i) + '.jpg', 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

for j in range(1,21):
    downPic(j)
