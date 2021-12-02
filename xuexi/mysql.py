# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : test1.py
# 开发工具 : PyCharm

import random
import pymysql

evo_conn = pymysql.connect(host="172.31.236.126", user="root", password="root123", charset="utf8")
evo_cursor = evo_conn.cursor()
evo_cursor.execute(
    'SELECT * FROM evo_wes_basic.basic_sku WHERE id in(SELECT sku_id FROM evo_wes_inventory.level3_inventory ) ORDER BY RAND() LIMIT 3;')
a = evo_cursor.fetchall()
sku_name1 = random.choice(a)[3]
sku_code1 = random.choice(a)[2]
print(a)
print(sku_code1)

