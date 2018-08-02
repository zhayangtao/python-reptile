# coding: utf-8
"""
爬虫调度器：初始化各个模块，然后通过 crawl(root_url)传入入口 url，
方法内容部实现按照运行流程控制各个模块的工作。
"""
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager


class SpiderMan:
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口 url
        self.manager.add_new_url(root_url)
        # 判断 url 管理器是否有新的 url，同时判断抓去了多少 url
        while self.manager.has_new_url() and self.manager.old_url_size() < 100:
            try:
                # 从 URL 管理器获取新的 url
                new_url = self.manager.get_new_url()
                # 从 html 下载器下载网页
                html = self.downloader.download(new_url)
                # print(html)
                # 从 html 解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                # 将抽取的 url 添加到 URl 管理器
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print("crawl failed")
        self.output.output_html()


if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")
