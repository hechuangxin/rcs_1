# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
from flask import abort, jsonify, Flask, request, Response
import json
import xml.sax
import pymysql
import random
import time
# from xml.dom.minidom import parse
# import xml.dom.minidom
app = Flask(__name__)
# 增加配置，支持中文显示
# app.config['JSON_AS_ASCII'] = False
# task01 ='<?xml version="1.0" encoding="UTF-8" ?> \
# <header /> \
# <body> \
# <success>{}</success> \
# <code>{}</code> \
# <message>Return success</message> \
# </body>'
#
# task01 = task01.format('aaaa','bbb')
#
# print(task01 )

'''
#工作提供接口
@app.route('/fh/authorized/workRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def work_task01():
    time_stamp = int(time.time())
    time1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    evo_conn = pymysql.connect(host="172.31.236.3", user="root", password="root123", charset="utf8")
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    a = evo_cursor.fetchall()
    sku_name1 = random.choice(a)[3]
    sku_code1 = random.choice(a)[2]
    quality = random.choice(a)[4]
    mfg_date = random.choice(a)[5]
    exp_date = random.choice(a)[6]
    inv_type = random.choice(a)[7]
    vendor_code = random.choice(a)[8]
    po_no = random.choice(a)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    b = evo_cursor.fetchall()
    sku_name2 = random.choice(b)[3]
    sku_code2 = random.choice(b)[2]
    quality2 = random.choice(b)[4]
    mfg_date2 = random.choice(b)[5]
    exp_date2 = random.choice(b)[6]
    inv_type2 = random.choice(b)[7]
    vendor_code2 = random.choice(b)[8]
    po_no2 = random.choice(b)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    c = evo_cursor.fetchall()
    sku_name3 = random.choice(c)[3]
    sku_code3 = random.choice(c)[2]
    quality3 = random.choice(c)[4]
    mfg_date3 = random.choice(c)[5]
    exp_date3 = random.choice(c)[6]
    inv_type3 = random.choice(c)[7]
    vendor_code3 = random.choice(c)[8]
    po_no3 = random.choice(c)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    d = evo_cursor.fetchall()
    sku_name4 = random.choice(d)[3]
    sku_code4 = random.choice(d)[2]
    quality4 = random.choice(d)[4]
    mfg_date4 = random.choice(d)[5]
    exp_date4 = random.choice(d)[6]
    inv_type4 = random.choice(d)[7]
    vendor_code4 = random.choice(d)[8]
    po_no4 = random.choice(d)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    e = evo_cursor.fetchall()
    sku_name5 = random.choice(e)[3]
    sku_code5 = random.choice(e)[2]
    quality5 = random.choice(e)[4]
    mfg_date5 = random.choice(e)[5]
    exp_date5 = random.choice(e)[6]
    inv_type5 = random.choice(e)[7]
    vendor_code5 = random.choice(e)[8]
    po_no5 = random.choice(e)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    f = evo_cursor.fetchall()
    sku_name6 = random.choice(f)[3]
    sku_code6 = random.choice(f)[2]
    quality6 = random.choice(f)[4]
    mfg_date6 = random.choice(f)[5]
    exp_date6 = random.choice(f)[6]
    inv_type6 = random.choice(f)[7]
    vendor_code6 = random.choice(f)[8]
    po_no6 = random.choice(f)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    g = evo_cursor.fetchall()
    sku_name7 = random.choice(g)[3]
    sku_code7 = random.choice(g)[2]
    quality7 = random.choice(g)[4]
    mfg_date7 = random.choice(g)[5]
    exp_date7 = random.choice(g)[6]
    inv_type7 = random.choice(g)[7]
    vendor_code7 = random.choice(g)[8]
    po_no7 = random.choice(g)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    h = evo_cursor.fetchall()
    sku_name8 = random.choice(h)[3]
    sku_code8 = random.choice(h)[2]
    quality8 = random.choice(h)[4]
    mfg_date8 = random.choice(h)[5]
    exp_date8 = random.choice(h)[6]
    inv_type8 = random.choice(h)[7]
    vendor_code8 = random.choice(h)[8]
    po_no8 = random.choice(h)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    j = evo_cursor.fetchall()
    sku_name9 = random.choice(j)[3]
    sku_code9 = random.choice(j)[2]
    quality9 = random.choice(j)[4]
    mfg_date9 = random.choice(j)[5]
    exp_date9 = random.choice(j)[6]
    inv_type9 = random.choice(j)[7]
    vendor_code9 = random.choice(j)[8]
    po_no9 = random.choice(j)[9]
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT c.bucket_code,c.lot_id,c.sku_code,c.sku_name,lot.lot_att02,lot.lot_att04,lot.lot_att05,lot.lot_att06,lot.lot_att07,lot.lot_att08 FROM evo_wes_inventory.lot AS lot RIGHT JOIN (SELECT a.lot_id,a.bucket_code,b.sku_code,b.sku_name FROM evo_wes_inventory.level3_inventory as a LEFT JOIN evo_wes_basic.basic_sku as b ON a.sku_id=b.id WHERE a.zone_code = "kckq" AND a.quantity > 2) AS c ON lot.id=c.lot_id ORDER BY RAND() LIMIT 1;')
    k = evo_cursor.fetchall()
    sku_name10 = random.choice(k)[3]
    sku_code10 = random.choice(k)[2]
    quality10 = random.choice(k)[4]
    mfg_date10 = random.choice(k)[5]
    exp_date10 = random.choice(k)[6]
    inv_type10 = random.choice(k)[7]
    vendor_code10 = random.choice(k)[8]
    po_no10 = random.choice(k)[9]
    get_value = request.get_data()
    print(get_value)
    return ('<?xml version="1.0" encoding="UTF-8"?>\
<root>\
    <header>\
        <appid>FH001</appid>\
        <appkey>vip@FH001</appkey>\
        <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
        <warehouse>VIP_NH</warehouse>\
        <version>1.0</version>\
    </header>\
    <body>\
        <item>\
            <id>{}1</id>\
            <warehouse_code>VIP_NH</warehouse_code>\
            <source_code>VIPS</source_code>\
            <destination_code>FH</destination_code>\
            <action_type>NEW</action_type>\
            <work_no>test{}-1</work_no>\
            <work_type>FLOWPICK_S</work_type>\
            <action_time>{}</action_time>\
            <remark>1211</remark>\
            <line_count>2</line_count>\
            <container_count>0</container_count>\
            <inf_function>1</inf_function>\
            <priority>0</priority>\
            <details>\
                <item>\
                    <id>1{}</id>\
                    <container_code/>\
                    <item_code>{}</item_code>\
                    <item_desc>{}</item_desc>\
                    <brand_name>brand001{}</brand_name>\
                    <item_cat1_code>cat1code01{}</item_cat1_code>\
                    <item_cat1_name>cat101{}</item_cat1_name>\
                    <item_cat2_code>cat2code01{}</item_cat2_code>\
                    <item_cat2_name>cat201{}</item_cat2_name>\
                    <item_cat3_code>cat3code01{}</item_cat3_code>\
                    <item_cat3_name>cat301{}</item_cat3_name>\
                    <unit_item>EACH</unit_item>\
                    <item_size><![CDATA[A]]></item_size>\
                    <item_color><![CDATA[红色]]></item_color>\
                    <item_spec_class>VAL,FRG</item_spec_class>\
                    <gross_weight>5.000</gross_weight>\
                    <net_weight>5.000</net_weight>\
                    <weight_um>g</weight_um>\
                    <volume>6000.000</volume>\
                    <volume_um>cm3</volume_um>\
                    <img>123</img>\
                    <qty>1</qty>\
                    <warehouse_code>VIP_NH</warehouse_code>\
                    <company_code>VIPS</company_code>\
                    <quality>{}</quality>\
                    <mfg_date>{}</mfg_date>\
                    <exp_date>{}</exp_date>\
                    <inv_type>{}</inv_type>\
                    <vendor_code>{}</vendor_code>\
                    <po_no>{}</po_no>\
                </item>\
                <item>\
                            <id>2{}</id>\
                            <container_code/>\
                            <item_code>{}</item_code>\
                            <item_desc>{}</item_desc>\
                            <brand_name>brand{}</brand_name>\
                            <item_cat1_code>cat1code02{}</item_cat1_code>\
                            <item_cat1_name>cat102{}</item_cat1_name>\
                            <item_cat2_code>cat2code02{}</item_cat2_code>\
                            <item_cat2_name>cat202{}</item_cat2_name>\
                            <item_cat3_code>cat3code02{}</item_cat3_code>\
                            <item_cat3_name>cat302{}</item_cat3_name>\
                            <unit_item>EACH</unit_item>\
                            <item_size><![CDATA[A]]></item_size>\
                            <item_color><![CDATA[红色]]></item_color>\
                            <item_spec_class>VAL,FRG</item_spec_class>\
                            <gross_weight>5.000</gross_weight>\
                            <net_weight>5.000</net_weight>\
                            <weight_um>g</weight_um>\
                            <volume>6000.000</volume>\
                            <volume_um>cm3</volume_um>\
                            <img>{}</img>\
                            <qty>1</qty>\
                            <warehouse_code>VIP_NH</warehouse_code>\
                            <company_code>VIPS</company_code>\
                            <quality>{}</quality>\
                            <mfg_date>{}</mfg_date>\
                            <exp_date>{}</exp_date>\
                            <inv_type>{}</inv_type>\
                            <vendor_code>{}</vendor_code>\
                            <po_no>{}</po_no>\
            </item>\
    </details>\
    </item>\
    <item>\
        <id>{}3</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-3</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
            <item>\
                    <id>33{}</id>\
                    <container_code/>\
                    <item_code>{}</item_code>\
                    <item_desc>{}</item_desc>\
                    <brand_name>brand03{}</brand_name>\
                    <item_cat1_code>cat1code03{}</item_cat1_code>\
                    <item_cat1_name>cat103{}</item_cat1_name>\
                    <item_cat2_code>cat2code03{}</item_cat2_code>\
                    <item_cat2_name>cat203{}</item_cat2_name>\
                    <item_cat3_code>cat3code03{}</item_cat3_code>\
                    <item_cat3_name>cat303{}</item_cat3_name>\
                    <unit_item>EACH</unit_item>\
                    <item_size><![CDATA[A]]></item_size>\
                    <item_color><![CDATA[红色]]></item_color>\
                    <item_spec_class>VAL,FRG</item_spec_class>\
                    <gross_weight>5.000</gross_weight>\
                    <net_weight>5.000</net_weight>\
                    <weight_um>g</weight_um>\
                    <volume>6000.000</volume>\
                    <volume_um>cm3</volume_um>\
                    <img>123</img>\
                    <qty>7</qty>\
                    <warehouse_code>VIP_NH</warehouse_code>\
                    <company_code>VIPS</company_code>\
                    <quality>{}</quality>\
                    <mfg_date>{}</mfg_date>\
                    <exp_date>{}</exp_date>\
                    <inv_type>{}</inv_type>\
                    <vendor_code>{}</vendor_code>\
                    <po_no>{}</po_no>\
            </item>\
    </details>\
    </item>\
    <item>\
        <id>{}4</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-4</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
            <item>\
                        <id>4{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand04{}</brand_name>\
                        <item_cat1_code>cat1code04{}</item_cat1_code>\
                        <item_cat1_name>cat104{}</item_cat1_name>\
                        <item_cat2_code>cat2code04{}</item_cat2_code>\
                        <item_cat2_name>cat204{}</item_cat2_name>\
                        <item_cat3_code>cat3code04{}</item_cat3_code>\
                        <item_cat3_name>cat304{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}5</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-5</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>5{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand05{}</brand_name>\
                        <item_cat1_code>cat1code05{}</item_cat1_code>\
                        <item_cat1_name>cat105{}</item_cat1_name>\
                        <item_cat2_code>cat2code05{}</item_cat2_code>\
                        <item_cat2_name>cat205{}</item_cat2_name>\
                        <item_cat3_code>cat3code05{}</item_cat3_code>\
                        <item_cat3_name>cat305{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}6</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-6</work_no>\
        <work_type>FLOWPICK_MS</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>6{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand06{}</brand_name>\
                        <item_cat1_code>cat1code06{}</item_cat1_code>\
                        <item_cat1_name>cat106{}</item_cat1_name>\
                        <item_cat2_code>cat2code06{}</item_cat2_code>\
                        <item_cat2_name>cat206{}</item_cat2_name>\
                        <item_cat3_code>cat3code06{}</item_cat3_code>\
                        <item_cat3_name>cat306{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}7</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-7</work_no>\
        <work_type>FLOWPICK_S</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>7{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand07{}</brand_name>\
                        <item_cat1_code>cat1code07{}</item_cat1_code>\
                        <item_cat1_name>cat107{}</item_cat1_name>\
                        <item_cat2_code>cat2code07{}</item_cat2_code>\
                        <item_cat2_name>cat207{}</item_cat2_name>\
                        <item_cat3_code>cat3code07{}</item_cat3_code>\
                        <item_cat3_name>cat307{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>123</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}8</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-8</work_no>\
        <work_type>FLOWPICK_S</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>8{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand08{}</brand_name>\
                        <item_cat1_code>cat1code08{}</item_cat1_code>\
                        <item_cat1_name>cat108{}</item_cat1_name>\
                        <item_cat2_code>cat2code08{}</item_cat2_code>\
                        <item_cat2_name>cat208{}</item_cat2_name>\
                        <item_cat3_code>cat3code08{}</item_cat3_code>\
                        <item_cat3_name>cat308{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>{}</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}9</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-9</work_no>\
        <work_type>FLOWPICK_S</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>9{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand09{}</brand_name>\
                        <item_cat1_code>cat1code09{}</item_cat1_code>\
                        <item_cat1_name>cat109{}</item_cat1_name>\
                        <item_cat2_code>cat2code09{}</item_cat2_code>\
                        <item_cat2_name>cat209{}</item_cat2_name>\
                        <item_cat3_code>cat3code09{}</item_cat3_code>\
                        <item_cat3_name>cat309{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>{}</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
    </details>\
    </item>\
    <item>\
        <id>{}10</id>\
        <warehouse_code>VIP_NH</warehouse_code>\
        <source_code>VIPS</source_code>\
        <destination_code>FH</destination_code>\
        <action_type>NEW</action_type>\
        <work_no>test{}-10</work_no>\
        <work_type>FLOWPICK_S</work_type>\
        <action_time>{}</action_time>\
        <remark>1211</remark>\
        <line_count>1</line_count>\
        <container_count>0</container_count>\
        <inf_function>1</inf_function>\
        <priority>0</priority>\
        <details>\
                <item>\
                        <id>100{}</id>\
                        <container_code/>\
                        <item_code>{}</item_code>\
                        <item_desc>{}</item_desc>\
                        <brand_name>brand10{}</brand_name>\
                        <item_cat1_code>cat1code10{}</item_cat1_code>\
                        <item_cat1_name>cat110{}</item_cat1_name>\
                        <item_cat2_code>cat2code10{}</item_cat2_code>\
                        <item_cat2_name>cat210{}</item_cat2_name>\
                        <item_cat3_code>cat3code10{}</item_cat3_code>\
                        <item_cat3_name>cat310{}</item_cat3_name>\
                        <unit_item>EACH</unit_item>\
                        <item_size><![CDATA[A]]></item_size>\
                        <item_color><![CDATA[红色]]></item_color>\
                        <item_spec_class>VAL,FRG</item_spec_class>\
                        <gross_weight>5.000</gross_weight>\
                        <net_weight>5.000</net_weight>\
                        <weight_um>g</weight_um>\
                        <volume>6000.000</volume>\
                        <volume_um>cm3</volume_um>\
                        <img>{}</img>\
                        <qty>1</qty>\
                        <warehouse_code>VIP_NH</warehouse_code>\
                        <company_code>VIPS</company_code>\
                        <quality>{}</quality>\
                        <mfg_date>{}</mfg_date>\
                        <exp_date>{}</exp_date>\
                        <inv_type>{}</inv_type>\
                        <vendor_code>{}</vendor_code>\
                        <po_no>{}</po_no>\
                </item>\
            </details>\
        </item>\
    </body>\
</root>'.format(time_stamp, time_stamp, time1, time_stamp, sku_code1, sku_name1, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, quality, mfg_date, exp_date, inv_type, vendor_code, po_no,
                time_stamp, 6920052501, '【补水加量】水漾肌密细肤水保湿2件套 收缩毛孔爽肤水补水', time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp,time_stamp, '/picture/6920052501xiao.png', 100, '2021-10-02', '2025-10-01', '3PL', 107827, 3731657826,
                time_stamp, time_stamp, time1, time_stamp, sku_code10, sku_name10, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, quality10, mfg_date10, exp_date10, inv_type10, vendor_code10, po_no10,
                time_stamp, time_stamp, time1, time_stamp, sku_code3, sku_name3, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, quality3, mfg_date3, exp_date3, inv_type3, vendor_code3, po_no3,
                time_stamp, time_stamp, time1, time_stamp, sku_code4, sku_name4, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, quality4, mfg_date4, exp_date4, inv_type4, vendor_code4, po_no4,
                time_stamp, time_stamp, time1, time_stamp, sku_code5, sku_name5, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, quality5, mfg_date5, exp_date5, inv_type5, vendor_code5, po_no5,
                time_stamp, time_stamp, time1, time_stamp, sku_code6, sku_name6, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, quality6, mfg_date6, exp_date6, inv_type6, vendor_code6, po_no6,
                time_stamp, time_stamp, time1, time_stamp, 6920040407, '【提拉轮廓】紧致肌密抗皱保湿修护淡纹洁面水乳精华护肤品套装女', time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, '/picture/6920040407da.jpg', 100, '2021-09-02', '2025-09-01', '3PL', 107827, 3731657826,
                time_stamp, time_stamp, time1, time_stamp, 6948043434526, '【补水 速润】珀莱雅 海洋活能密集爽肤水 保湿水 135ml', time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, '/picture/6948043434526zhong.jpg', 100, '2021-12-02', '2025-12-01', '3PL', 107827, 3731657826,
                time_stamp, time_stamp, time1, time_stamp, 6920052501, '【补水加量】水漾肌密细肤水保湿2件套 收缩毛孔爽肤水补水', time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, time_stamp, '/picture/6920052501xiao.png', 100, '2021-10-02', '2025-10-01', '3PL', 107827, 3731657826, ))
'''
#工作提供握手接口
@app.route('/fh/authorized/postReceivedWork', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def work_task02():
    time_stamp = int(time.time())
    work_task02 = request.get_data()
    print(work_task02)
    # DOMTree = xml.dom.minidom.parse(get_value02)
    # province_data = DOMTree.documentElement
    # provinces = get_value02.getElementsByTagName("id")
    # print(provinces)
    return ('<?xml version="1.0" encoding="utf-8"?>\
    <root>\
  <header>\
    <appid>FH001</appid>\
    <appkey>vip@FH001</appkey>\
    <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
    <version>1.0</version>\
  </header>\
 <body>\
    <item>\
      <msgcode>{}</msgcode>\
      <msg><![CDATA[Success]]></msg>\
      <id>233</id>\
    </item>\
    <item>\
      <msgcode>001{}</msgcode>\
      <id>233</id>\
    </item>\
  </body>\
</root>'.format(time_stamp,time_stamp))

#工作反馈接口
@app.route('/fh/authorized/postCompletedWork', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def work_task03():
    time_stamp = int(time.time())
    work_task03 = request.get_data()
    print(work_task03)
    # DOMTree = xml.dom.minidom.parse(get_value02)
    # province_data = DOMTree.documentElement
    # provinces = get_value02.getElementsByTagName("id")
    # print(provinces)
    return ('<?xml version="1.0" encoding="utf-8"?>\
    <root>\
  <header>\
    <appid>FH001</appid>\
    <appkey>vip@FH001</appkey>\
    <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
    <version>1.0</version>\
  </header>\
 <body>\
    <item>\
      <msgcode>{}</msgcode>\
      <msg><![CDATA[Success]]></msg>\
      <id>233</id>\
    </item>\
    <item>\
      <msgcode>001{}</msgcode>\
      <id>233</id>\
    </item>\
  </body>\
</root>'.format(time_stamp,time_stamp))


#事件提供接口
@app.route('/fh/authorized/eventRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_task03():
    time_stamp = int(time.time())
    time1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    evo_conn = pymysql.connect(host="172.31.236.126", user="root", password="root123", charset="utf8")
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT work_no FROM evo_vip.vip_work WHERE work_type = "OUB_SHIP_PICK" AND state = "WAITING_EVENT" ORDER BY rand() LIMIT 3;')
    a = evo_cursor.fetchall()
    work_no = random.choice(a)[0]
    get_value = request.get_data()
    print(get_value)
    return ('<root>\
    <header>\
        <appid>FH001</appid>\
        <appkey>vip@FH001</appkey>\
        <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
        <warehouse>VIP_NH</warehouse>\
        <version>1.0</version>\
    </header>\
    <body>\
        <item>\
            <id>1{}</id>\
            <warehouse_code>VIP_NH</warehouse_code>\
            <source_code>VIPS</source_code>\
            <destination_code>FH</destination_code>\
            <event_type>OUB_SHIP_PICK_START</event_type>\
            <reference_type />\
            <reference_no>{}</reference_no>\
            <action_time>{}</action_time>\
            <remark />\
            <reference/>\
        </item>\
    </body>\
</root>'.format(time_stamp,work_no,time1))

#事件提供握手接口
@app.route('/fh/authorized/postReceivedEvent', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_task04():
    evo_conn = pymysql.connect(host="172.31.236.126", user="root", password="root123", charset="utf8")
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT event_id FROM evo_vip.vip_event WHERE event_type = "OUB_SHIP_PICK_START" AND state="NEW" ORDER BY rand() LIMIT 3;')
    a = evo_cursor.fetchall()
    event_id = random.choice(a)[0]
    time_stamp = int(time.time())
    get_value02 = request.get_data()
    print(get_value02)
    # DOMTree = xml.dom.minidom.parse(get_value02)
    # province_data = DOMTree.documentElement
    # provinces = get_value02.getElementsByTagName("id")
    # print(provinces)
    return ('<?xml version="1.0" encoding="utf-8"?>\
    <root>\
  <header>\
    <appid>FH001</appid>\
    <appkey>vip@FH001</appkey>\
    <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
    <version>1.0</version>\
  </header>\
 <body>\
    <item>\
      <msgcode>{}</msgcode>\
      <msg><![CDATA[Success]]></msg>\
      <id>233</id>\
    </item>\
    <item>\
      <msgcode>001{}</msgcode>\
      <id>233</id>\
    </item>\
  </body>\
</root>'.format(event_id,time_stamp))


#事件反馈接口
@app.route('/fh/authorized/eventInfoRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def event_task03():
    time_stamp = int(time.time())
    event_task03 = request.get_data()
    print(event_task03)
    # DOMTree = xml.dom.minidom.parse(get_value02)
    # province_data = DOMTree.documentElement
    # provinces = get_value02.getElementsByTagName("id")
    # print(provinces)
    return ('<?xml version="1.0" encoding="utf-8"?>\
    <root>\
  <header>\
    <appid>FH001</appid>\
    <appkey>vip@FH001</appkey>\
    <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
    <version>1.0</version>\
  </header>\
 <body>\
    <item>\
      <msgcode>S00</msgcode>\
      <msg><![CDATA[Success]]></msg>\
      <id>1630488156</id>\
    </item>\
  </body>\
</root>')


#交接反馈接口
@app.route('/fh/authorized/postCompletedWorkContainer', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def Container_task03():
    time_stamp = int(time.time())
    Container_task03 = request.get_data()
    print(Container_task03)
    # DOMTree = xml.dom.minidom.parse(get_value02)
    # province_data = DOMTree.documentElement
    # provinces = get_value02.getElementsByTagName("id")
    # print(provinces)
    return ('<?xml version="1.0" encoding="utf-8"?>\
    <root>\
  <header>\
    <appid>FH001</appid>\
    <appkey>vip@FH001</appkey>\
    <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
    <version>1.0</version>\
  </header>\
 <body>\
    <item>\
      <msgcode>{}</msgcode>\
      <msg><![CDATA[Success]]></msg>\
      <id>233</id>\
    </item>\
    <item>\
      <msgcode>001{}</msgcode>\
      <id>233</id>\
    </item>\
  </body>\
</root>'.format(time_stamp,time_stamp))


#周转箱查询接口
@app.route('/fh/authorized/basContainerRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def Container():
    time_stamp = int(time.time())
    Container = request.get_data()
    print(Container)
    # DOMTree = xml.dom.minidom.parse(get_value02)
    # province_data = DOMTree.documentElement
    # provinces = get_value02.getElementsByTagName("id")
    # print(provinces)
    return ('<?xml version="1.0" encoding="UTF-8"?>\
<root>\
    <header>\
        <appid>FH001</appid>\
        <appkey>vip@FH001</appkey>\
        <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
        <warehouse>VIP_NH</warehouse>\
        <version>1.0</version>\
    </header>\
    <body>\
        <item>\
            <msgcode>S00</msgcode>\
            <msg><![CDATA[Success]]></msg>\
            <warehouse>VIP_NH</warehouse>\
            <source_code>VIPS</source_code>\
            <destination_code>FH</destination_code>\
            <container_code>121</container_code>\
            <available_work_types>\
                <work_type>OUB_SALE_SS_PICK</work_type>\
    <work_type>OUB_SALE_SM_PICK</work_type>\
    <work_type>OUB_SALE_MM_PICK</work_type>\
    <work_type>OUB_SALE_MM_SINGLE_PICK</work_type>\
    <work_type>OUB_SALE_EX_PICK</work_type>\
    <work_type>OUB_SHIP_EX_PICK</work_type>\
    <work_type>INV_MOVE_OUT</work_type>\
    <work_type>FLOWPICK_FN</work_type>\
    <work_type>FLOWPICK_LN</work_type>\
                <work_type>OUB_SHIP_PICK</work_type>\
                <work_type>FLOWPICK_MS</work_type>\
                <work_type>FLOWPICK_S</work_type>\
                <work_type>FLOWPICK_N</work_type>\
            </available_work_types>\
            <used>0</used>\
        </item>\
    </body>\
</root>')


# wes = {
# 	"success": 'true',
# 	"data": [{
# 		"id": "7001",
# 		"success": 'true'
# 	}]
# }
# wes = {
# 	"success": "true",
# 	"body": {
# 		"id ": "7001",
# 		"success": "true",
#         "id ": "7001",
# 		"success": "false"
# 	}
# }
# @app.route('/apicallback/quicktron/wms/job', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/sl
# def get_wes():
#     get_value = json.loads(request.get_data(as_text=True))
#     print(get_value)
#     return jsonify(wes)

if __name__ == '__main__':
    app.run(host = '172.31.253.14',port = 1234,debug = True)