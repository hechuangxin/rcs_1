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



#工作提供接口
@app.route('/fh/authorized/workRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_task01():
    time_stamp = int(time.time())
    time1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    evo_conn = pymysql.connect(host="172.31.238.143", user="root", password="root123", charset="utf8")
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT * FROM evo_wes_basic.basic_sku WHERE state = "effective" AND sn_enabled = 0 ORDER BY rand() LIMIT 3;')
    a = evo_cursor.fetchall()
    sku_name = random.choice(a)[3]
    sku_code = random.choice(a)[2]
    get_value = request.get_data()
    print(get_value)
    return ('<?xml version="1.0" encoding="UTF-8"?>\
<root>\
    <header>\
        <appid>FH001</appid>\
        <appkey>vip@FH001</appkey>\
        <request_id>5a9281c9-0773-4cbf-a777-c4bff0b2e02d</request_id>\
        <warehouse>VIP_ZZ</warehouse>\
        <version>1.0</version>\
    </header>\
    <body>\
        <item>\
            <id>{}</id>\
            <warehouse_code>VIP_NH</warehouse_code>\
            <source_code>VIPS</source_code>\
            <destination_code>FH</destination_code>\
            <action_type>NEW</action_type>\
            <work_no>VIPS{}</work_no>\
            <work_type>OUB_SHIP_PICK</work_type>\
            <action_time>{}</action_time>\
            <remark>1211</remark>\
            <line_count>1</line_count>\
            <container_count>1</container_count>\
            <priority>0</priority>\
            <details>\
                <item>\
                    <id>001{}</id>\
                    <container_code>HTIK{}</container_code>\
                    <item_code>{}</item_code>\
                    <item_desc>{}</item_desc>\
                    <brand_name>brand{}</brand_name>\
                    <item_cat1_code>cat1code{}</item_cat1_code>\
                    <item_cat1_name>cat1{}</item_cat1_name>\
                    <item_cat2_code>cat2code{}</item_cat2_code>\
                    <item_cat2_name>cat2{}</item_cat2_name>\
                    <item_cat3_code>cat3code{}</item_cat3_code>\
                    <item_cat3_name>cat3{}</item_cat3_name>\
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
                    <qty>10</qty>\
                    <warehouse_code>VIP_ZZ</warehouse_code>\
                    <company_code>VIPS</company_code>\
                    <po_no>2000199271</po_no>\
                    <vendor_code>100023</vendor_code>\
                    <inv_type>Normal</inv_type>\
                    <quality>100</quality>\
                </item>\
            </details>\
        </item>\
    </body>\
</root>'.format(time_stamp,time_stamp,time1,time_stamp,time_stamp,sku_code,sku_name,time_stamp,time_stamp,time_stamp,time_stamp,time_stamp,time_stamp,time_stamp))

#工作提供握手接口
@app.route('/fh/authorized/postReceivedWork', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_task02():
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
</root>'.format(time_stamp,time_stamp))

#事件提供接口
@app.route('/fh/authorized/eventRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_task03():
    time_stamp = int(time.time())
    time1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    evo_conn = pymysql.connect(host="172.31.238.143", user="root", password="root123", charset="utf8")
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
        <warehouse>VIP_ZZ</warehouse>\
        <version>1.0</version>\
    </header>\
    <body>\
        <item>\
            <id>11928</id>\
            <warehouse_code>VIP_ZZ</warehouse_code>\
            <source_code>VIPS</source_code>\
            <destination_code>FH</destination_code>\
            <event_type>INV_FULL_DIFF_RESERVE</event_type>\
            <reference_type />\
            <reference_no/>\
            <action_time>{}</action_time>\
            <remark />\
            <reference>\
                <reserve_time>2021-08-26 12:00:00.000</reserve_time>\
            </reference>\
        </item>\
        <item>\
            <id>11929</id>\
            <warehouse_code>VIP_ZZ</warehouse_code>\
            <source_code>FH</source_code>\
            <destination_code>VIPS</destination_code>\
            <event_type>OUB_SHIP_PICK_START</event_type>\
            <reference_type />\
            <reference_no>{}</reference_no>\
            <action_time>{}</action_time>\
            <remark />\
            <reference/>\
        </item>\
    </body>\
</root>'.format(time1,work_no,time1))

#事件提供握手接口
@app.route('/fh/authorized/postReceivedEvent', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_task04():
    evo_conn = pymysql.connect(host="172.31.238.143", user="root", password="root123", charset="utf8")
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




wes = {
	"success": 'true',
	"data": [{
		"id": "7001",
		"success": 'true'
	}]
}
@app.route('/apicallback/quicktron/wms/job', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/sl
def get_wes():
    get_value = json.loads(request.get_data(as_text=True))
    print(get_value)
    return jsonify(wes)

if __name__ == '__main__':
    app.run(host = '172.31.219.121',port = 1234,debug = True)