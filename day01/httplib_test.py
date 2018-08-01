class SpiderMain:
    def __init__(self):
        self.urls = ''


'''
负责管理深度 URL 链接以及去重
'''


class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.used_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.used_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        temp_url = self.new_urls.pop()
        self.used_urls.add(temp_url)
        return temp_url


'''
负责对指定的 URL 网页内容进行下载获取
'''
from urllib import request, parse
from bs4 import BeautifulSoup
import re


class HtmlDownLoader:
    def download(self, url):
        if url is None:
            return None
        resp = request.urlopen(url)
        if resp.getCode() != 200:
            return None
        return resp.read()


'''
负责解析网页内容
'''


class HtmlParser:
    def parse(self, url, content, html_encode='utf-8'):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding=html_encode)

    def _get_new_urls(self, url, soup: BeautifulSoup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/\w+'))
        for link in links:
            url_path = link['href']
            new_url = parse.urljoin(url, url_path)
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, url, soup):
        return
