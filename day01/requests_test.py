import requests
import chardet
import json

url = 'http://www.baidu.com'
r = requests.get(url)
print(chardet.detect(r.content))
r.encoding = chardet.detect(r.content)['encoding']
print(r.text)

# 流模式
rStream = requests.get(url, stream=True)
print(r.raw.read(10))

'''
使用第三方 requests
'''
headers = {"AppId": "dbd170e5-990a-4ee4-b539-95b0f972286c",
           "Referer": "http://172.16.1.140/cloudmm/issue/live.html",
           "AppSecret": "zoLGVgiEPjb8utSpihnh"}
postData = {"limit": 10, "pageSize": 2}
# get 请求
url2 = 'http://172.16.1.140/ymmopenapi/sgw/v1/fqa/list'
resp = requests.get(url2, params=postData, headers=headers)
print(resp.raise_for_status())  # 当返回的状态码是 4xx 或 5xx 时，抛出异常
print(resp.status_code)  # 接口返回的状态码
print(resp.headers)  # 消息头
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

# 重定向与历史信息
r = requests.get(url)
print(r.url)
print(r.status_code)
print(r.history)