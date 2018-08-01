from lxml import etree
from beautifulSoup_test import html_str


html = etree.HTML(html_str)
result = etree.tostring(html)
print(result)
