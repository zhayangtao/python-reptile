# coding:utf-8
import re
from urllib import parse
from bs4 import BeautifulSoup


class HtmlParser:
    """
    html 解析器
    """

    def parser(self, page_url, html_cont):
        """
        用于解析网页内容，抽取 URL 和数据
        :param page_url: 下载页面的 URL
        :param html_cont: 下载的网页内容
        :return:
        """
        if not page_url or not html_cont:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup: BeautifulSoup):
        """
        抽取新的 url 集合
        :param page_url: 下载页面的 URL
        :param soup: soup
        :return: 返回新的 URL 集合
        """
        new_urls = set()
        # 抽取符合要求的 a 标记
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            # 提取 href 属性
            new_url = link['href']
            # 拼接成完整网址
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup: BeautifulSoup):
        """
        抽取有效数据
        :param page_url: 下载页面的 URL
        :param soup:
        :return: 返回有效数据
        """
        data = {'url': page_url}
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        # 获取 tag 中包含的所有文本内容
        data['summary'] = summary.get_text()
        return data


if __name__ == '__main__':
    string = ''
    string2 = None
    if not string:
        print('not string ')
    if not string2:
        print('none string2')
