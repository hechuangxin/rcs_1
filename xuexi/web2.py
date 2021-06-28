# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
from urllib import parse

import urllib.request
import json
import ast

url = "http://172.31.236.33:7011/evo/tetris/warehouseBasic/warehouse/page"

headers = {


    "Connection": "keep-alive",

    "Pragma": "no-cache",

    "Cache-Control": "no-cache",

    "Accept": "*/*",

    "X-Requested-With": "XMLHttpRequest",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",

    "Referer": "http://172.31.236.33/web/basic/basic/organization/warehouse?paging.current=1&paging.pageSize=10",

    "Accept-Encoding": "gzip, deflate",

    "Accept-Language": "zh-CN,zh;q=0.9",

    "Cookie": "EGG_SESS=DW-nkVs9l6ZjU0tpyXVrDpOpi6Ed58ehroo4wntKUss9eZ1R-lff9CDZ384d3Vlsg5yuhHvbYypS6ki0iaP8TyqetZ2v-J9rcWCX_lZ2zfIDwxsv7V_230FF119DIdKeF_oVJoJUZcGqXhPJPZXTabq-fQmwYmvOl64YCDFkwC5ZbzP1zzUppxleiNFO7KBAASBrSzJqLzdPYUocwZ_atRjkOTOKv1Rz4S1WuRmLDa_FeLMC8dn333MVFEoveqQMl-DamX1fKVuSPB40QjO2W5bgh1C9SqYgsmlPX7PEobGUuRiA6C8p8oZrr-nTrSWaUcfJENIpcu9bZ874GNYbR-Bu0XsAXFw3Wejbx5EZEV5yyuCavxLNKzTf-KEEWPtj"

}

# url 作为Request()方法的参数，构造并返回一个Request对象

request = urllib.request.Request(url)

# Request对象作为urlopen()方法的参数，发送给服务器并接收响应

response = urllib.request.urlopen(request)

html = response.read().decode('utf-8')
a= json.loads(html)

print(html)
print(type(html))
print(a)
print(type(a))
# print(a['blocks'])
# print(type(a['blocks']))
# print((',').join(str(x) for x in a))













# b= a['blocks']
# c= b[2]
# print(type(c))
# print(c)
# d=c.values()
# print(d)
# for v in d:
#     if type(v)==str:
#         print(v)
#         if type(v)==list:
#             for e in v:
#                 print(e.values())

