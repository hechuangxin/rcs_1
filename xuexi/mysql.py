# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : test1.py
# 开发工具 : PyCharm


import pymysql
db = pymysql.connect(host='172.31.238.117',user='root',password='root123',charset='utf-8',
                     cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
cursor.execute('slect * from evo_rcs.basic_agv')