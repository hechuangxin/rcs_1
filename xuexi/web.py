# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
# from urllib import request  # 导入request模块
# import chardet  # 导入chardet编码识别模块
#
# if __name__ == "__main__":
#     response = request.urlopen("http://172.31.236.33/evo/getMenus?localePrefix=client.&locale=zh-CN")  # 打开网站
#     html = response.read()  # 读取内容
#
#     charset = chardet.detect(html)  # 获取编码格式
#     html = html.decode(charset["encoding"])  # 解码
#     print(html)
import requests
import json

args_data = {
        'id':'321',
        'name':'cba'
}
url='http://172.31.236.33:7011/evo/tetris/warehouseBasic/warehouse/page'
pdata = json.dumps(args_data)
headers = {'Content-Type': 'application/json',"Cookie":"EGG_SESS=DW-nkVs9l6ZjU0tpyXVrDpOpi6Ed58ehroo4wntKUss9eZ1R-lff9CDZ384d3Vlsg5yuhHvbYypS6ki0iaP8TyqetZ2v-J9rcWCX_lZ2zfIDwxsv7V_230FF119DIdKeF_oVJoJUZcGqXhPJPZXTabq-fQmwYmvOl64YCDFkwC5ZbzP1zzUppxleiNFO7KBAASBrSzJqLzdPYUocwZ_atdBzzdX_A_3lniLuaG-jKKOy7GTcVAgl6UyXLdjpVkjttqDnZYkJvi4-6-o57M5EH5SgJCbEi6RVNzk-xRS9-SrvEOfruGhltmKladoAStJIDK_6DTfiGSVjvY-fQcLUIYhHb804SS5xOYrCKS07oc_xkRFLnG_qd8kWMh4Jz1BA"}
res = requests.get(url, data=pdata, headers=headers)
print(res.text)
print(type(res))
