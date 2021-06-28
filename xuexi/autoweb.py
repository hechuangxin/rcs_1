from urllib import request
from http import cookiejar

# 1.创建cookie的实例对象
cookie = cookiejar.CookieJar()
# 2.创建cookie处理器,也就CookieHandler
handler = request.HTTPCookieProcessor(cookie)
# 3.通过CookieHandler创建opener
opener = request.build_opener(handler)
# 4.使用opender的open方法打开网页
response = opener.open('http://172.31.236.33/evo/getMenus?localePrefix=client.&locale=zh-CN')
# 打印cookie信息
for item in cookie:
    print('Name = %s' % item.name)
    print('Value = %s' % item.value)
