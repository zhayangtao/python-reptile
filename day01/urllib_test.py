from urllib import parse, request
from urllib.request import urlopen
import json

url = 'http://172.16.1.140/ymmopenapi/sgw/v1/fqa/list'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) ' \
             'Version/11.0 Mobile/15A372 Safari/604.1 '
headers = {"AppId": "dbd170e5-990a-4ee4-b539-95b0f972286c",
           "Referer": "http://172.16.1.140/cloudmm/issue/live.html",
           "AppSecret": "zoLGVgiEPjb8utSpihnh"}
postData = {"limit": 10, "page": 1}
data = json.dumps(postData).encode(encoding='utf-8')  # json 格式
textData = parse.urlencode(postData).encode(encoding="utf8")
req = request.Request(url, headers=headers)
resp = urlopen(req)
html = resp.read()
print(html.decode(encoding='utf-8'))

'''
使用第三方 requests
'''
import requests

# get 请求
resp = requests.get(url, params=postData, headers=headers)
print(resp.url)
print(resp.text)
print(resp.json())

postUrl = "http://172.16.1.140/ymmopenapi/sgw/v1/fqa/acs"
headers = {
    "AppId": "dbd170e5-990a-4ee4-b539-95b0f972286c",
    "AppSecret": "zoLGVgiEPjb8utSpihnh",
    "x-auth-token": "9c9879ac-81e4-473f-bfd3-212a6f6f5ba9"
}
postData2 = {"refId": "409065116", "type": "Support", "supportType": "Course"}
# post 请求
resp = requests.post(postUrl, data=json.dumps(postData2), headers=headers)
print(resp.json())

