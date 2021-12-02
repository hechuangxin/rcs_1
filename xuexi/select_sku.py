# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
import pymysql
import random

#连接数据库
evo_conn = pymysql.connect(host="172.31.236.126",user="root", password="root123", charset="utf8")
evo_cursor = evo_conn.cursor()
evo_cursor.execute('SELECT b.container_code,a.work_no FROM evo_vip.vip_work as a,evo_vip.vip_work_detail as b WHERE a.id = b.work_id AND b.state = "NEW" ORDER BY rand() LIMIT 3;')
a = evo_cursor.fetchall()
sku_id = random.choice(a)[0]
print(sku_id)