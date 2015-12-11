import requests
from lxml import etree
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
def downPic(n):
    a = requests.get('http://www.meizitu.com/a/list_1_' + str(n) + '.html',headers=headers)
    selector = etree.HTML(a.text)
    content = selector.xpath('//*[@id="maincontent"]/div[1]/ul/li/div/div/a/@href')
    k = 1
    for each in content:
        print(each)
        page_content = requests.get(each,headers=headers)
        img_selector = etree.HTML(page_content.text)
        img_urls = img_selector.xpath('//*[@id="picture"]/p/img/@src')
        i = 1
        for url in img_urls:
            img_content = requests.get(url,headers=headers)
            fp = open('/Users/1akang/Desktop/hello/' + str(n) + '-' + str(k) + '-' + str(i) + '.jpg', 'wb')
            fp.write(img_content.content)
            fp.close()
            i += 1
        k += 1

for j in range(1, 21):
    downPic(j)
