# 存储为 json
import requests
from bs4 import BeautifulSoup
import json

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers=headers)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
content = []
for mulu in soup.find_all(class_='mulu'):
    h2 = mulu.find('h2')
    if h2:
        h2_title = h2.string  # 获取标题
        # print(h2_title)
        list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            print(href, box_title)
            list.append({'href': href, 'box_title': box_title})
        content.append({'title': h2_title, 'content': list})

string = [{"username": "七夜", "age": 24}, (1, 2), 3]
json_str = json.dumps(string, ensure_ascii=False)
print(json_str)
with open('qiye.txt', 'w') as fp:
    json.dump(content, fp=fp, ensure_ascii=False)

new_str = json.loads(json_str)
print(new_str)
with open('qiye.txt', 'r') as fp:
    print(json.load(fp))

from urllib import request
from lxml import etree
import requests


def schedule(blocknum, blocksize, totalsize):
    '''
    :param blocknum:已经下载的数据块
    :param blocksize:数据块的大小
    :param totalsize:远程文件的大小
    :return:
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前下载进度：%d' % per)


user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers=headers)
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src')
i = 0
for img_url in img_urls:
    request.urlretrieve(img_url, 'img' + str(i) + '.jpg', schedule)
    i += 1
