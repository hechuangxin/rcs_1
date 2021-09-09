# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
import pymysql
import random
import time
evo_conn = pymysql.connect(host="172.31.236.126", user="root", password="root123", charset="utf8")
evo_cursor = evo_conn.cursor()
evo_cursor.execute(
    'SELECT * FROM evo_wes_basic.basic_sku WHERE state = "effective" AND sn_enabled = 0 ORDER BY rand() LIMIT 3;')
a = evo_cursor.fetchall()
work_no = random.choice(a)
print(work_no)

# time_stamp = int(time.time())
# print(time_stamp)



# print('<?xml version="1.0" encoding="UTF-8"?>\
# <root>\
#     <header>\
#         <appid>FH001</appid>\
#         <appkey>vip@FH001</appkey>\
#         <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
#         <warehouse>VIP_NH</warehouse>\
#         <version>1.0</version>\
#     </header>\
#     <body>\
#         <item>\
#             <id>{}</id>\
#             <warehouse_code>VIP_NH</warehouse_code>\
#             <source_code>VIPS</source_code>\
#             <destination_code>VIPS</destination_code>\
#             <action_type>NEW</action_type>\
#             <work_no>VIPS{}</work_no>\
#             <work_type>INB_RC_SHELF</work_type>\
#             <action_time>2015-03-28 14:21:88.000</action_time>\
#             <remark>1211</remark>\
#             <line_count>1</line_count>\
#             <container_count>1</container_count>\
#             <priority>0</priority>\
#             <details>\
#                 <item>\
#                     <id>id{}</id>\
#                     <container_code>HTIK{}</container_code>\
#                     <item_code>{}</item_code>\
#                     <item_desc>sku{}</item_desc>\
#                     <brand_name>brand{}</brand_name>\
#                     <item_cat1_code>cat1code{}</item_cat1_code>\
#                     <item_cat1_name>cat1{}</item_cat1_name>\
#                     <item_cat2_code>cat2code{}</item_cat2_code>\
#                     <item_cat2_name>cat2{}</item_cat2_name>\
#                     <item_cat3_code>cat3code{}</item_cat3_code>\
#                     <item_cat3_name>cat3{}</item_cat3_name>\
#                     <unit_item>EACH</unit_item>\
#                     <item_size><![CDATA[A]]></item_size>\
#                     <item_color><![CDATA[红色]]></item_color>\
#                     <item_spec_class>VAL,FRG</item_spec_class>\
#                     <gross_weight>5.000</gross_weight>\
#                     <net_weight>5.000</net_weight>\
#                     <weight_um>g</weight_um>\
#                     <volume>6000.000</volume>\
#                     <volume_um>cm3</volume_um>\
#                     <img></img>\
#                     <qty>100</qty>\
#                     <warehouse_code>VIP_NH</warehouse_code>\
#                     <company_code>VIPS</company_code>\
#                     <po_no>2000199271</po_no>\
#                     <vendor_code>100023</vendor_code>\
#                     <inv_type>Normal</inv_type>\
#                     <quality>100</quality>\
#                     <mfg_date>2015-01-01</mfg_date>\
#                     <exp_date>2018-01-01</exp_date>\
#                     <inv_lot_no />\
#                 </item>\
#             </details>\
#         </item>\
#     </body>\
# </root>'.format(1,2,3,4,5,6,7,8,9,10,11,12,13))