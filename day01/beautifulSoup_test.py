"""
beautifulSoup 测试
"""
from bs4 import BeautifulSoup
import re

html_str = """
<html><head><title>The Dormouse's story</title></head
<body>
<p class="title"><b> The Dormouse's story </b></p>
<p class="story">Once upon a time there were three little sisters; and their names
were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
<a href="http://example.com/lacie" class="sister" id="link2"><!--lacie--></a>and
<a href="http://example.com/tillie" class="sister" id="1ink3">Tillie</a>i
and they lived at the bottom of a well.</p>
<p class="story" >...</p>
"""

# 创建 BeautifulSoup 对象
soup = BeautifulSoup(html_str, features='lxml', from_encoding='utf-8')
print(soup.prettify())
print(soup.p.get('class'))
print(soup.p.string)
print(soup.a.string)
print(soup.strings)
for string in soup.strings:
    print(repr(string))
print('-------------')
print(soup.a.next_sibling)
print(soup.find_all('a'))
print(soup.find_all(True))
print(soup.find_all(id='link2'))
print(soup.find_all(href=re.compile('elsie'), id='link1'))
# 有些 tag 属性在搜索中不能使用，比如 data-* 属性
data_soup = BeautifulSoup('<div data-foo="value">foo1</div>', features='lxml')
# data_soup.find_all(data-foo="value")
print(data_soup.find_all(attrs={'data-foo': 'value'}))
print('---------')
print(soup.find_all("a", limit=2))
# css 选择器
print('-----------------css 选择器-----------------')
print(soup.select("title"))
print(soup.select("html head title"))
print(soup.select("head > title"))
print(soup.select("p > #link1"))
# 查找兄弟节点
print(soup.select("#link1 ~ .sister"))
print(soup.select("#link1 + .sister"))