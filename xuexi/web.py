# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
#get接口调用
import urllib.request
# import urllib2

get_url = "http://172.31.236.33/evo/tetris/warehouseBasic/warehouse/page"
cookie_headers = {
        "Cookie" : "EGG_SESS=DW-nkVs9l6ZjU0tpyXVrDpOpi6Ed58ehroo4wntKUss9eZ1R-lff9CDZ384d3Vlsg5yuhHvbYypS6ki0iaP8TyqetZ2v-J9rcWCX_lZ2zfIDwxsv7V_230FF119DIdKeF_oVJoJUZcGqXhPJPZXTabq-fQmwYmvOl64YCDFkwC5ZbzP1zzUppxleiNFO7KBAASBrSzJqLzdPYUocwZ_ata24iUINzsmqCRzWKyO-SbT76SxqX0LeIoSpoAG6cgnPkehnRdcn1iuXOTvOrYVuDUXWzBMsO6UDFz3aXYvCS8UulZQhuifRL4K8VC0hnnQgX3rk4I8K_cTh1XU4OqTSfnFr6dxYkmWsYtB3I0CuzqTHcfV323nrSuCtKp5dtq16; locale=zh-cn"
}
req = urllib2.Request(url=get_url,headers=cookie_headers)
res_data = urllib2.urlopen(req)
res = res_data.read()
print(res)

# a = urllib.request.urlopen("www.baidu.com")
