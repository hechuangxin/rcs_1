# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : test1.py
# 开发工具 : PyCharm


import pymysql
db = pymysql.connect(host='172.31.238.117',user='root',password='root123',charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
cursor.execute('SELECT agv_code FROM evo_rcs.basic_agv WHERE id=1')
a=cursor.fetchall()
for b in a:
    print(b)
