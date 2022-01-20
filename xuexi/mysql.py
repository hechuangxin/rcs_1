# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : test1.py
# 开发工具 : PyCharm

import random
import pymysql

# evo_conn = pymysql.connect(host="172.31.236.3", user="root", password="root123", charset="utf8")
# evo_cursor = evo_conn.cursor()
# evo_cursor.execute(
#     'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq") AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 2;')
# a = evo_cursor.fetchall()
# sku_name1 = random.choice(a)[3]
# sku_code1 = random.choice(a)[2]
# print(a)
# print(sku_code1)

evo_conn = pymysql.connect(host="172.31.236.3", user="root", password="root123", charset="utf8")
evo_cursor = evo_conn.cursor()
evo_cursor.execute(
    'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq") AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 5;')
a = evo_cursor.fetchall()
sku_name1 = random.choice(a)[3]
sku_code1 = random.choice(a)[2]
quality = random.choice(a)[4]
mfg_date = random.choice(a)[5]
exp_date = random.choice(a)[6]
inv_type = random.choice(a)[7]
vendor_code = random.choice(a)[8]
po_no = random.choice(a)[9]
print(a)
b=str(a)
print(b)
print(b.split(','))
print(type(b.split(',')))
c=b.split(',')
print(c.remove(','))

print(sku_name1)


